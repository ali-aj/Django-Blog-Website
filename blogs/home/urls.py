from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/<str:blog_id>', views.display_blog, name='display_blog'),
    path('<int:blog_id>', views.delete_blog, name='delete_blog'),
] 
