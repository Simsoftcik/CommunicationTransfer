from django.shortcuts import render
from django.views.generic import DetailView
from .forms import *
from django.shortcuts import render
from .models import BidSystem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import BidCategory
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

is_edited = True

@login_required(login_url='login')
def my_systems(request):
    user_id = request.user.id
    bid_systems = BidSystem.query_objects.filter(user_id=user_id)
    

    if request.method == 'POST':
        form = BidSystemForm(request.POST)
        if form.is_valid():
            bid_system = form.save(commit=False)
            bid_system.user_id = request.user
            bid_system.save()
    else:
        form = BidSystemForm()
    
    return render(request, 'bid_systems/my_systems.html', {'form': form, 'bid_systems': bid_systems})

class selected_system(DetailView):
    model = BidSystem
    template_name = 'bid_systems/selected_system.html'
    context_object_name = 'system'

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        system = self.get_object()

        # Pobierz kategorie dla tego systemu
        categories = system.bidcategory_set.all()

        category_data = {}

        # Iteruj przez kategorie
        for category in categories:
            # Pobierz sytuacje dla bieżącej kategorii
            situations = category.bidsituation_set.all()

            # Słownik do przechowywania sytuacji wraz z ofertami
            situation_data = {}

            # Iteruj przez sytuacje w bieżącej kategorii
            for situation in situations:
                # Pobierz oferty dla bieżącej sytuacji
                bids = situation.bid_set.all()
                situation_data[situation] = bids

            # Dodaj do słownika danych kategorii (sytuacje wraz z ofertami)
            category_data[category] = situation_data

        context['categories'] = categories
        context['category_data'] = category_data

        return context

class edit_system(DetailView):
    model = BidSystem
    template_name = 'bid_systems/edit_system.html'
    context_object_name = 'system'
    


    def get_context_data(self, **kwargs):
        categories = BidCategory.query_objects.filter(bid_system_id=self.object)
        context = super().get_context_data(**kwargs)
        system_id = self.object
        context = super().get_context_data(**kwargs)
        context['category_form'] = BidCategoryForm(instance=self.object, system_id=system_id)
        context['situation_form'] = BidSituationForm(instance=self.object, system_id=system_id)
        context['bid_form'] = BidForm(instance=self.object)
        context['categories'] = categories
        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        category_form = BidCategoryForm(request.POST, system_id=self.object.id)
        if category_form.is_valid():
            category_form.save()

        situation_form = BidSituationForm(request.POST, system_id=self.object.id)
        if situation_form.is_valid():
            situation_form.save()

        bid_form = BidForm(request.POST, system_id=self.object.id)
        if bid_form.is_valid():
            bid_form.save()

        return render(request, self.template_name, self.get_context_data())



