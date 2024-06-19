
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

    def clean_w_clubs(self):
        return self.validate_card_string(self.cleaned_data['w_clubs'], 'W clubs')

    def clean_w_diamonds(self):
        return self.validate_card_string(self.cleaned_data['w_diamonds'], 'W diamonds')

    def clean_w_hearts(self):
        return self.validate_card_string(self.cleaned_data['w_hearts'], 'W hearts')

    def clean_w_spades(self):
        return self.validate_card_string(self.cleaned_data['w_spades'], 'W spades')

    def clean_n_clubs(self):
        return self.validate_card_string(self.cleaned_data['n_clubs'], 'N clubs')

    def clean_n_diamonds(self):
        return self.validate_card_string(self.cleaned_data['n_diamonds'], 'N diamonds')

    def clean_n_hearts(self):
        return self.validate_card_string(self.cleaned_data['n_hearts'], 'N hearts')

    def clean_n_spades(self):
        return self.validate_card_string(self.cleaned_data['n_spades'], 'N spades')

    def clean_e_clubs(self):
        return self.validate_card_string(self.cleaned_data['e_clubs'], 'E clubs')

    def clean_e_diamonds(self):
        return self.validate_card_string(self.cleaned_data['e_diamonds'], 'E diamonds')

    def clean_e_hearts(self):
        return self.validate_card_string(self.cleaned_data['e_hearts'], 'E hearts')

    def clean_e_spades(self):
        return self.validate_card_string(self.cleaned_data['e_spades'], 'E spades')

    def clean_s_clubs(self):
        return self.validate_card_string(self.cleaned_data['s_clubs'], 'S clubs')

    def clean_s_diamonds(self):
        return self.validate_card_string(self.cleaned_data['s_diamonds'], 'S diamonds')

    def clean_s_hearts(self):
        return self.validate_card_string(self.cleaned_data['s_hearts'], 'S hearts')

    def clean_s_spades(self):
        return self.validate_card_string(self.cleaned_data['s_spades'], 'S spades')

    def validate_card_string(self, value, field_name):
        valid_characters = set('0123456789TJQKA')
        if not all(char in valid_characters for char in value):
            raise forms.ValidationError(f"{field_name} contains invalid characters.")
        return value


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