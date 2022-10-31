"""edtech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login", views.LoginPage.as_view(), name="login"),
    path("register",views.RegisterPage.as_view(), name="register"),
    path("address", views.AddressPage.as_view(), name="address"),
    path("home", views.HomePage.as_view(), name="home"),
    path("home1", views.HomePage1.as_view(), name="home1"),
    path("logout", views.LogoutPage.as_view(), name="logout"),
    path("content",views.CoursecontentPage.as_view(), name="content"),
    path("course-detail/<int:pk>",views.CourseDetails.as_view(), name="course-detail"),
    path("quiz",views.QuizPage.as_view(), name="quiz"),
]
