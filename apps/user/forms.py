from django import forms
from django.conf import settings
from .models import User
class SignUpForm(forms.Form):
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'First name','maxlength':settings.TEXTBOXMAXLENGTH}),
        required=True,
        error_messages={'required':"First name is required"}
    )
    last_name = forms.CharField(
        label='Last name',
        widget=forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Last name','maxlength':settings.TEXTBOXMAXLENGTH}),
        required=True,
        error_messages={'required':"Last name is required"}
    )
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'Email','maxlength':settings.TEXTBOXMAXLENGTH}),
        required=True,
        error_messages={'required':"Email is required"}
    )
    password = forms.CharField(
        label='Password',
        widget=forms.TextInput(attrs={'class':'form-control','type':'password','placeholder':'Password','maxlength':settings.TEXTBOXMAXLENGTH, 'autocomplete':'off'}),
        required=True,
        error_messages={'required':"Password is required"}
    )
    confirm_password = forms.CharField(
        label='Confirm password',
        widget=forms.TextInput(attrs={'class':'form-control','type':'password','placeholder':'Password','maxlength':settings.TEXTBOXMAXLENGTH, 'autocomplete':'off'}),
        required=True,
        error_messages={'required':"Password confirmation is required"}
    )
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electronico ya existe")
        return email

class LoginForm(forms.Form):
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'class':'form-control','type':'email','maxlength':settings.TEXTBOXMAXLENGTH}),
        required=True,
        error_messages={'required':"Email is required"}
    )
    password = forms.CharField(
        label='Password',
        widget=forms.TextInput(attrs={'class':'form-control','type':'password','maxlength':settings.TEXTBOXMAXLENGTH, 'autocomplete':'off'}),
        required=True,
        error_messages={'required':"Password is required"}
    )