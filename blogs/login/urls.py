from django.urls import path
from . import views

urlpatterns = [
    path('', views.forget_password_view, name='forget_password'),
]
