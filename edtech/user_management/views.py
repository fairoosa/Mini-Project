from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterationForm, AddressRegisterationForm, UserLoginForm
from Course.models import Course, CourseContent,  Quiz


class LoginPage(generic.TemplateView):
    template_name = "login.html"
    form_class = UserLoginForm

    def post(self, request, *args, **kwagrs):
        print(self.request.POST)  
        username = self.request.POST['username']
        password = self.request.POST['password']
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy("home")) 
        else:
            print("incorrect username and password")
            return redirect(reverse_lazy("register"))
           
      


class RegisterPage(generic.CreateView):
    template_name = "register.html"
    form_class = UserRegisterationForm
    success_url = '/login'



class AddressPage(generic.CreateView):
    template_name="address.html"
    form_class =  AddressRegisterationForm
    success_url = '/login'


class HomePage(generic.ListView):
    template_name = "home.html"
    model = Course


class HomePage1(generic.ListView):
    template_name = "home1.html"
    model = Course


class LogoutPage(generic.View):

    def get(self, request, *args, **kwagrs):
        print(self.request.GET)
        logout(request) 
        return redirect(reverse_lazy("login"))


class CourseDetails(generic.DetailView):
    template_name = "coursedetail.html"
    model=Course

class CoursecontentPage(generic.ListView):
    template_name = "coursecontent.html"
    model=CourseContent

class QuizPage(generic.ListView):
    template_name = "quiz.html"
    model=Quiz


    