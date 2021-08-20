from django.urls import path
from .views import html_form
urlpatterns = [
    path('html-form/', html_form, name='html_form')
]
