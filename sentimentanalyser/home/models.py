from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self):
        return self.username


class Analysis(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='analyses'
    )

    input_text = models.TextField()

    sentiment = models.CharField(
        max_length=10,
    )

    polarity = models.FloatField()

    subjectivity = models.FloatField()

    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.sentiment}"