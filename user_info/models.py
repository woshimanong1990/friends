from django.db import models
from django.contrib.auth.models import User


class UserInfo(models):
    user = models.OneToOneField(User)
    user_name = models.CharField()
    gender = models.CharField()
    age = models.IntegerField()
    birthday = models.DateField()
    enable = models.BooleanField(default=True)
    live_location = models.CharField()
    desire_location = models.CharField()
    educational_background = models.IntegerField()
    year_income = models.IntegerField()
    email = models.EmailField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class UserImage(models):
    user = models.ForeignKey(User)
    enable = models.BooleanField(default=True)
    url = models.URLField()


class IDCard(models):
    user = models.OneToOneField(User)
    number = models.CharField()
    is_authenticated = models.BooleanField(default=False)


class PhoneInfo(models):
    phone_number = models.CharField()
    device_type = models.CharField()
    device_id = models.CharField()

class Customer(models):
    username = models.CharField()
    password = models.CharField()
    

class LoginToken(models):
    pass

class