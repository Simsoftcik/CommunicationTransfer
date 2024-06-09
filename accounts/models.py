from django.db import models
from django.contrib.auth.models import User

class Accounts(models.Model):
    sex = (
        ('Male','Male'),
        ('Female','Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, blank=True)
    gender = models.CharField(blank = True, null = True, choices = sex, max_length=100, default='gender')
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='default_profile_pic.jpg')
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    about_you = models.TextField( null=True, blank=True)
