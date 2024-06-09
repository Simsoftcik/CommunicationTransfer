from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='Untitled')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/', blank=True)

    n_clubs = models.CharField(max_length=30, blank=True)
    n_diamonds = models.CharField(max_length=30, blank=True)
    n_hearts = models.CharField(max_length=30, blank=True)
    n_spades = models.CharField(max_length=30, blank=True)

    e_clubs = models.CharField(max_length=30, blank=True)
    e_diamonds = models.CharField(max_length=30, blank=True)
    e_hearts = models.CharField(max_length=30, blank=True)
    e_spades = models.CharField(max_length=30, blank=True)

    s_clubs = models.CharField(max_length=30, blank=True)
    s_diamonds = models.CharField(max_length=30, blank=True)
    s_hearts = models.CharField(max_length=30, blank=True)
    s_spades = models.CharField(max_length=30, blank=True)

    w_clubs = models.CharField(max_length=30, blank=True)
    w_diamonds = models.CharField(max_length=30, blank=True)
    w_hearts = models.CharField(max_length=30, blank=True)
    w_spades = models.CharField(max_length=30, blank=True)

class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='comments/', blank=True)
