from django.urls import path
from .views import *

urlpatterns = [
            path('my_systems/', my_systems), 
            path('my_systems/<int:pk>/', selected_system.as_view(), name='selected_system'),
            path('my_systems/e<int:pk>/', edit_system.as_view(), name='edit_system'),
        ]