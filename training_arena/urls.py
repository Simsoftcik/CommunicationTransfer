from django.urls import path
from .views import opening, generate_new_hand_id

urlpatterns = [
    path('opening/', opening, name='opening'),
    path('generate_new_hand_id/', generate_new_hand_id, name='generate_new_hand_id')
    ]