from django.urls import path, include
from django.conf import settings
from .import views as todo_view
from django.conf.urls.static import static
from django.contrib.auth import views as auth

urlpatterns = [
        path('', todo_view.home, name = 'home'),
        path('todo/', todo_view.todo, name = 'todo'),
        path('todo/details/<int:id>', todo_view.details, name = 'details'),
        path('update/<str:item_id>', todo_view.update, name = 'update'),
        path('del/<str:item_id>', todo_view.remove, name = 'del'),
        path('search/', todo_view.SearchResultsViews.as_view(), name = 'search'),
        
        #this part is for user authentication routes(urls)
        path('login/', todo_view.login, name = 'login'),
        path('logout/', auth.LogoutView.as_view(template_name = 'todo/todo.html'), name = 'logout'),
        path('register/', todo_view.register, name = 'register'),
        path('password-reset/', auth.PasswordResetView.as_view(template_name = 'todo/password_reset.html'), name = 'password_reset'),
        path('password-reset/', auth.PasswordResetView.as_view(template_name = 'todo/password_reset_email.html'), name = 'password_reset'),
        path('password-reset/done/', auth.PasswordResetDoneView.as_view(template_name = 'todo/password_reset_done.html'), name = 'password_reset_done'),
        path('password-reset-confirm/<uidb64>/<token>/', auth.PasswordResetConfirmView.as_view(template_name='todo/password_reset_confirm.html'),name='password_reset_confirm'),
        path('password-reset-complete/', auth.PasswordResetCompleteView.as_view(template_name = 'todo/password_reset_complete.html'), name = 'password_reset_complete'),
        ]

