
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
        # if self.system_id is not None:
            # self.fields['bid_system_id'] = forms.ModelChoiceField(
            #     queryset=BidSystem.query_objects.all(),
            #     initial=self.system_id,
            #     widget=forms.HiddenInput()
            # )
        if self.instance.pk:  # Check if instance exists (for editing)
            self.fields['bid_system_id'].initial = self.instance.bid_system_id_id
        
        self.fields['bid_system_id'] = forms.ModelChoiceField(
            queryset=BidSystem.query_objects.all(),
            initial=self.system_id,
            widget=forms.HiddenInput()
        )
        
        categories = BidCategory.query_objects.filter(bid_system_id=self.system_id)
        
        self.fields['bid_category_id'] = forms.ModelChoiceField(
                queryset=categories,
                widget=forms.Select(),  
                label='Bid Category',
                # empty_label=None
            )

        self.fields['bid_category_id'].label_from_instance = lambda obj: f"{obj.name}"  


    class Meta:
        model = BidSituation
        exclude = ['bid_system_id'] 
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
            self.fields['bid_system_id'] = forms.ModelChoiceField(
                queryset=BidSystem.query_objects.all(),
                initial=self.system_id,
                widget=forms.HiddenInput()
            )

        situations = BidSituation.query_objects.filter(bid_system_id=self.system_id)
        self.fields['bid_situation_id'] = forms.ModelChoiceField(
                queryset=situations,
                widget=forms.Select(),  
                label='Bid Situation',
                # empty_label=None
            )
        # if self.system_id is not None:
        #     categories = BidCategory.query_objects.filter(bid_system_id=self.system_id)
        #     situations = BidSituation.objects.filter(bid_category_id__in=categories)

        #     self.fields['bid_situation_id'].queryset = situations

    class Meta:
        model = Bid
        exclude = ['bid_system_id']
        widgets = {
            'name': TextInput(attrs={
                'class': '',
                'placeholder': 'Situation...'
            }),
            'symbol': Select(attrs={
                'class': '',
                'placeholder': 'Symbol'
            }),
            'forcing_type': Select(attrs={
                'class': '',
                'placeholder': 'Forcing type'
            }),
            'strength': TextInput(attrs={
                'class': '',
                'placeholder': 'Strength (optional)'
            }),
            'description': Textarea(attrs={
                'class': '',
                'placeholder': 'Description...'
            })
        }

    def label_from_instance(self, obj):
        return f"{obj.name}"