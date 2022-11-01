from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeTodo, name='home-todo'),
    path('detail/<int:todoId>/', views.detailTodo, name='detail-todo'),
    path('create/', views.createTodo, name='create-todo'),
    path('update/<int:todoId>/', views.updateTodo, name='update-todo'),
    path('delete/<int:todoId>/', views.deleteTodo, name='delete-todo'),
]