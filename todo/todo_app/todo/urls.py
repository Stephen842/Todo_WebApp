from django.urls import path, include
from django.conf import settings
from .import views
from django.conf.urls.static import static

urlpatterns = [
        path('', views.home, name = 'home'),
        path('todo/', views.todo, name = 'todo'),
        path('del/<str:item_id>', views.remove, name = 'del'),
        ]

