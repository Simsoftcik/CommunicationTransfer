from django.urls import path
from .views import *

urlpatterns = [
            path('', forum),
            path('<int:pk>/', selected_post.as_view(), name='selected_post'),
            path('new_post', new_post.as_view(), name='create_post')
        ]