from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
#Create your models here.
class UserManager(BaseUserManager):

   def create_user(self,username,email,password = None):
   
   
        if username is None:
            raise TypeError('User should have a Username')
        if email is None:
            raise TypeError('User should have a Email')
    
   
        user= self.model(username = username,email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user



   def create_superuser(self,username,email,password = None):


        if password is None:
            raise TypeError('password should not be none')
    
        user= self.create_user(username,email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    
    

class User(AbstractBaseUser,PermissionsMixin):
     username = models.CharField(max_length=255,unique=True,db_index=True)
     email = models.EmailField(max_length=255,unique=True,db_index=True)
     is_verified=models.BooleanField(default=False)
     is_active=models.BooleanField(default=True)
     is_staff=models.BooleanField(default=False)
     creted_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)


     USERNAME_FIELD  = 'email'
     REQUIRED_FIELDS = ['username']

     objects = UserManager()

     def __str__(self):
          return self.username
     @property
     def tokens(self):
          refresh = RefreshToken.for_user(self)
          return {
              'refresh':str(refresh),
              'access':str(refresh.access_token)
          }
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=25,default='Your_Name')
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    experience = models.TextField(blank=True, null=True)

    def _str_(self):
        return f'{self.user.username} Profile'
