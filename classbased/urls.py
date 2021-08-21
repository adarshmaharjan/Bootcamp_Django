
from django.urls import path
from .views import FirstTemplate, FirstTemplateRedirect, FirstView, TemplateView
from .crud_views import Create, List, Detail, Update, Delete
app_name = 'classbased'
urlpatterns = [
    # classbased
    path('first/', FirstView.as_view()),
    path('first-test/', FirstTemplate.as_view()),
    path('template-redirect/', FirstTemplateRedirect.as_view()),
    path('create/', Create.as_view(), name='create'),
    path('list/', List.as_view(), name='list'),
    path('detail/<int:id>', Detail.as_view(), name='detail'),
    path('update/<int:id>', Update.as_view(), name='update'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),


]
