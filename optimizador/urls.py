from django.urls import path
from . import views

'''
Se añade url pattern para reconocer el ejecutable en view.py
'''
urlpatterns = [
    path('', views.load_and_optimize, name='load_and_optimize')
]