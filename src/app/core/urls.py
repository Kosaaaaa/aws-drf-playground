"""
URL mappings for the core API.
"""
from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('jokes/', views.GetJokes.as_view(), name='jokes'),
]
