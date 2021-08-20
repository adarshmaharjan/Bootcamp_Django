from django import urls
from django.urls import path
from .views import forms_home, django_form, django_model_form
urlpatterns = [
    path('home/', forms_home, name='home'),
    path('django-form/', django_form, name='django-form'),
    path('forms-model/', django_model_form, name='django-model-form'),
]
