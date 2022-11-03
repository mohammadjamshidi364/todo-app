from django.urls import path

from . import views

urlpatterns = [
    path('' , views.todoItems , name='todo_items'),
    path('create_new_item/', views.createItem , name="new_todo_item"),
    path('show_todo_item/<str:pk>/', views.showTodoItem , name='show_todo_item'),
    path('update_todo_item/<str:pk>/', views.updateItem , name="update_todo_item"),
    path('delete_todo_item/<str:pk>/', views.deleteTodoItem , name='delete_todo_item'),
]