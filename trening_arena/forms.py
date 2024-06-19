from django import forms
from trening_arena.util.enums import Bid

class WhatShouldOpen(forms.Form):
    CHOICES = [(bid.value, bid.value) for bid in Bid]
    guess = forms.ChoiceField(choices=CHOICES, label='What should you bid?', widget=forms.Select(attrs={'class': 'custom-select'}))

    

