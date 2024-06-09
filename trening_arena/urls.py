from django.urls import path
# from .views import *
from . import views

urlpatterns = [
    path('opening/', views.opening, name='opening'),
    path('generate_new_hand_id/', views.generate_new_hand_id, name='generate_new_hand_id')
    # path('/', views.arena)
    ]