from django.urls import path
from .views import delete_user_info, list_all_user, detail_view, create_user_info, update_user_info

app_name = 'crud'
urlpatterns = [
    # curd
    path('list/', list_all_user, name='list'),
    path('detail/<int:user_id>', detail_view, name='detail'),
    path('create/', create_user_info, name='create'),
    path('update/<int:user_id>', update_user_info, name='update'),
    path('delete/<int:user_id>', delete_user_info, name='delete')

]
