from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# extends abstract user because easiest way to hash password
# in settings AUTH_USER_MODEL = 'users.User'
class User(AbstractUser):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200,unique=True)
    password=models.CharField(max_length=200)
    username = None
    USERNAME_FIELD = 'email' # with this user can log in with email
    REQUIRED_FIELDS = []