from typing import Any
from django.contrib.auth import logout,authenticate, login
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import LoginForm,SignUpForm
from .models import User
from apps.utils import send_user_mail

# Create your views here.
class SignUpView(TemplateView):
    template_name = "user/register.html"

    def post(self,request,*args,**kwars):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = User()
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.email = form.cleaned_data.get("email")
            user.set_password(form.cleaned_data.get("password"))
            user.is_active=True
            user.save()
            if user:
                send_user_mail(form.cleaned_data.get("email"),'email/confirm.html','Bienvenido',"Gracias por registrarte con nosotros")
                messages.success(request,"El usuario ha sido creado correctamente")
            else:
                messages.error(request,"Error al crear el usuario")
        else:
            messages.error(request,form.errors)
            
        return redirect('register')


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = SignUpForm
        return context

class LoginView(TemplateView):
    template_name = "user/index.html"

    def post(self,request,*args,**kwars):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,"Error al iniciar sesión")
        else:
            messages.error(request,form.errors)
        
        return redirect('index')

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = SignUpForm
        return context