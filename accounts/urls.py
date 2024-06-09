from django.urls import path
from . import views

urlpatterns = [path('profile/', views.profile), 
               path('register/', views.register),
               path('logout/', views.logout)
               ]
