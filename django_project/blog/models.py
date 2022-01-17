from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# create database classes

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  # text field is for paragraphs and unrestricted length of text
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
