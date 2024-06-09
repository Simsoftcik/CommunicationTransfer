
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['user_id', 'date']
        labels = {
            'image': 'Upload Image'
        }
        widgets = {
            'n_clubs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'N clubs...'}),
            'n_diamonds': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'N diamonds...'}),
            'n_hearts': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'N Hearts...'}),
            'n_spades': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'N Spades...'}),
            'e_clubs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E clubs...'}),
            'e_diamonds': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E diamonds...'}),
            'e_hearts': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E Hearts...'}),
            'e_spades': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E Spades...'}),
            's_clubs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'S clubs...'}),
            's_diamonds': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'S diamonds...'}),
            's_hearts': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'S Hearts...'}),
            's_spades': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'S Spades...'}),
            'w_clubs': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'W clubs...'}),
            'w_diamonds': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'W diamonds...'}),
            'w_hearts': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'W Hearts...'}),
            'w_spades': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'W Spades...'}),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['user_id', 'date', 'post_id']
        labels = {
            'image': 'Upload Image'
        }
        widgets = {
            'content':Textarea(attrs={
                'class':'',
                'placeholder':'Write a comment...'
            }),
        }