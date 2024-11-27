from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('tags/', views.tag_list, name='tags'),
    path('tags/add/', views.add_tag, name='add_tag'),
    path('tags/<int:id>/update/', views.update_tag, name='update_tag'),
    path('tags/<int:id>/delete/', views.delete_tag, name='delete_tag'),
]