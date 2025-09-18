"""
URL configuration for Infosys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from blog.views import BlogpostView,BlogpostDetailView,BlogpostCreateView,BlogpostUpdateView,SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',BlogpostView.as_view(),name='blog'),
    path('blog/<int:id>/',BlogpostDetailView.as_view(),name='blog-detail'),
    path('blog/create/',BlogpostCreateView.as_view(),name='blog-create'),
    path('blog/<int:id>/update/',BlogpostUpdateView.as_view(),name='blog-update'),
    path('accounts/signup/',SignupView.as_view(),name='signup'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='blog/login.html',redirect_authenticated_user=True),name='login'),
    path('accounts/logout/',auth_views.LogoutView.as_view(template_name='blog/login.html',next_page='/accounts/login/'),name='logout'),
]