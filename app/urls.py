"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.urls import path, include
from app import views
urlpatterns = [
    path('', views.home, name='home')
]
