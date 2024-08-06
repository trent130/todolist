from django.urls import path
from. import views

app_name = "Todo"
urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("todo/<int:pk>/", views.todo_details, name="todo_details"),
    path("todo/<int:pk>/edit/", views.edit_todo, name="edit_todo"),
    path("todo/<int:pk>/delete/", views.delete_todo, name="delete_todo"),
]
