"""
URL configuration for blogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static
from login import views as login_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls')),
    path('contact_us/', views.contact_us, name='contact'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('', login_views.redirect_view),
    path('my_blogs/', views.my_blogs),
    path('login/', login_views.login_view, name="login"),
    path('register/', login_views.register_view),
    path('logout/', login_views.logout_view),
    path('forget_password/', include('login.urls')),
    path('my_blogs/blogs/<str:blog_id>', views.display_blog, name='display_blog'),
    path('delete/', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 