from django.db import models


class UserInformation(models.Model):
    first_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=6, unique=True)
    hobbies = models.CharField(max_length=60)
    about_me = models.TextField(max_length=1000)
