from django.urls import path, include
from django.conf import settings
from .import views
from django.conf.urls.static import static

urlpatterns = [
        path('', views.home, name = 'home'),
        path('todo/', views.todo, name = 'todo'),
        path('details/<int:item_id>', views.details, name = 'details'),
        path('update/<str:item_id>', views.update, name = 'update'),
        path('del/<str:item_id>', views.remove, name = 'del'),
        path('search/', views.SearchResultsViews.as_view(), name = 'search'),
        ]

