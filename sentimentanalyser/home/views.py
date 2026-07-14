from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from home.models import *
from textblob import TextBlob

def index(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        cpassword = request.POST.get('password2')

        name_parts = fullname.split(maxsplit=1)
        first_name = name_parts[0] if name_parts else ""
        last_name = name_parts[1] if len(name_parts) > 1 else ""

        if password != cpassword:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                last_name=last_name,
                first_name=first_name
            )
            user.save()
            messages.success(request, "Registration successful! Please login.")
            return redirect('login')
    return render(request, 'register.html')

def login(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            auth_login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid username or password.")

    return render(request, "login.html")


def dashboard(request):

    result = None

    if request.method == "POST":

        text = request.POST.get("text")

        blob = TextBlob(text)

        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        if polarity > 0:
            sentiment = "Positive"

        elif polarity < 0:
            sentiment = "Negative"

        else:
            sentiment = "Neutral"

        Analysis.objects.create(

            user=request.user,

            input_text=text,

            sentiment=sentiment,

            polarity=polarity,

            subjectivity=subjectivity

        )

        result = {

            "sentiment": sentiment,

            "polarity": round(polarity, 2),

            "subjectivity": round(subjectivity, 2)

        }

    analyses = Analysis.objects.filter(
        user=request.user
    ).order_by("-analyzed_at")

    context = {

        "result": result,

        "analyses": analyses

    }

    return render(request,"dashboard.html",context)


def logout(request):
    auth_logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

