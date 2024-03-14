from django.urls import path
from .views import LoginView, SignUpView


urlpatterns = [
    path('',LoginView.as_view(),name="index"),
    path('register',SignUpView.as_view(),name="register"),
    
]