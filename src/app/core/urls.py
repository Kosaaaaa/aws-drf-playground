"""
URL mappings for the core API.
"""
from core import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('jokes/', views.GetJokes.as_view(), name='jokes'),
]
