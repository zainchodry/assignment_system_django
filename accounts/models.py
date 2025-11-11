from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Role_Choices = [
        ('teacher', 'Teacher'),
        ('student', 'Student')
    ]
    role = models.CharField(max_length=20, choices=Role_Choices)
