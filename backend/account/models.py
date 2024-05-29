from django.db import models


class User(models.Model):
    ava = models.CharField(max_length=100)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
