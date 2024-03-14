from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from apps.core.models import AbstractBaseModel


class User(AbstractBaseUser,AbstractBaseModel):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=150,blank=True,null=True)
    last_name = models.CharField(max_length=150,blank=True,null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'