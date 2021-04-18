from django.urls import path
from todolist import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('status/<task_id>', views.change_status, name='change_status'),
]
