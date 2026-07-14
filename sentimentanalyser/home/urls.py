from django.urls import path
import home.views

urlpatterns = [
    path('', home.views.index, name = 'home'),
    path('register',home.views.register, name='register'),
    path('login',home.views.login, name='login'),
    path('dashboard',home.views.dashboard, name='dashboard'),
    path('logout', home.views.logout, name='logout'),
]