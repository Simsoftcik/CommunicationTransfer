
from django.forms import ModelForm, TextInput, Textarea, Select
from django import forms
from .models import *

class BidSystemForm(ModelForm):
    class Meta:
        model = BidSystem
        exclude = ['user_id', 'date']
        widgets = {
            'name':TextInput(attrs={
                'class':'',
                'placeholder':'Name of your system...'
            }),
            'description':Textarea(attrs={
                'class':'',
                'placeholder':'Decription, principles...'
            }),
        }

class BidCategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.system_id = kwargs.pop('system_id', None)
        super().__init__(*args, **kwargs)
        if self.system_id is not None:
            self.fields['bid_system_id'] = forms.ModelChoiceField(
                queryset=BidSystem.query_objects.all(),
                initial=self.system_id,
                widget=forms.HiddenInput()
            )

    class Meta:
        model = BidCategory
        exclude = []
        widgets = {
            'name': TextInput(attrs={
                'class': '',
                'placeholder': 'Name of your category...'
            })
        }


class BidSituationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.system_id = kwargs.pop('system_id', None)
        super().__init__(*args, **kwargs)
        
        categories = BidCategory.query_objects.filter(bid_system_id=self.system_id)
        
        # choices = [(category, category.name) for category in categories]
        
        # self.fields['bid_category_id'] = forms.ChoiceField(
        #         queryset=categories, 
        #         choices=choices, 
        #         widget=forms.Select, 
        #         required=True
        #     )
        # self.fields['bid_category_id'].queryset = categories
        
        self.fields['bid_category_id'] = forms.ModelChoiceField(
                queryset=categories,
                widget=forms.Select(),  
                label='Bid Category',
                # empty_label=None
            )

        self.fields['bid_category_id'].label_from_instance = lambda obj: f"{obj.name}"  


    class Meta:
        model = BidSituation
        exclude = []  # Usuwamy wyłączenie, aby uwzględnić wszystkie pola z modelu BidSituation
        widgets = {
            'name': TextInput(attrs={
                'class':'',
                'placeholder':'Name of your situation...'
            }),
            'sequences': TextInput(attrs={
                'class':'',
                'placeholder':'Bid sequences (optional)'
            }),
            'description': Textarea(attrs={
                'class':'',
                'placeholder':'description'
            })
        }


class BidForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.system_id = kwargs.pop('system_id', None)
        super().__init__(*args, **kwargs)

        if self.system_id is not None:
            categories = BidCategory.query_objects.filter(bid_system_id=self.system_id)
            situations = []
            for category in categories:
                situations.append(BidSituation.filter(bid_category_id=category))
            # situations = BidSituation.query_objects.filter(bid_category__in=categories)

            self.fields['Situation'] = forms.ModelChoiceField(
                queryset=situations,
                widget=forms.Select(attrs={'class': 'form-control'}),
                label='Bid Situation',
                # empty_label='Select a Bid Situation'  # Opcjonalna pusta etykieta
            )

            self.fields['Situation'].label_from_instance = lambda obj: f"{obj.name}"

    class Meta:
        model = Bid
        exclude = []
        widgets = {
            'name':TextInput(attrs={
                'class':'',
                'placeholder':'Situation...'
            }),
            'symbol':Select(attrs={
                'class':'',
                'placeholder':'Symbol'
            }),
            'forcing_type':Select(attrs={
                'class':'',
                'placeholder':'Forcing type'
            }),
            'strength':TextInput(attrs={
                'class':'',
                'placeholder':'Strength (optional)'
            }),
            'description':Textarea(attrs={
                'class':'',
                'placeholder':'Description...'
            })
        }
