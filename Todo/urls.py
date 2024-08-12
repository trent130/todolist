from django.urls import path
from. import views
from django.contrib.auth import views as auth_views

app_name = "Todo"
urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("todo/<int:pk>/", views.todo_details, name="todo_details"),
    path("todo/<int:pk>/edit/", views.edit_todo, name="edit_todo"),
    path("todo/<int:pk>/delete/", views.delete_todo, name="delete_todo"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.registerview, name="register"),
    path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uuidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("todo/delete/", views.delete_all_todo, name="delete_all_todo"),
]
