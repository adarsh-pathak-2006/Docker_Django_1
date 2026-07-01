from django.shortcuts import render, redirect
from django.views import View
from core.forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(View):
    def get(self, request):
        form=RegisterForm()
        return render(request, 'register.html', { 'form':form })
    
    def post(self, request):
        form_data=RegisterForm(request.POST)
        if form_data.is_valid():
            username=form_data.cleaned_data['username']
            password=form_data.cleaned_data['password']
            rep_password=form_data.cleaned_data['rep_password']

            if password==rep_password:
                if User.objects.filter(username=username).exists():
                    return render(request, 'register.html', { 'form':form_data ,'user_err':'user already exists' })
                else:
                    user=User.objects.create_user(username=username, password=password)
                    login(request, user)
                    return redirect('home')
            
            else:
                return render(request, 'register.html', { 'form':form_data, 'pass_err':'both the passowords must be same' })
            
        else:
            return render(request, 'register.html', { 'form':form_data, 'invalid':'invalid inputs' })

class LoginView(View):
    def get(self, request):
        form=LoginForm()
        return render(request, 'login.html', { 'form':form })
    
    def post(self, request):
        form_data=LoginForm(request.POST)
        if form_data.is_valid():
            username=form_data.cleaned_data['username']
            password=form_data.cleaned_data['password']

            user=authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('register')
            
        else:
            return render(request, 'login.html', { 'form':form_data, 'invalid':'invalid inputs' })
        

class HomeView(LoginRequiredMixin,TemplateView):
    template_name='home.html'