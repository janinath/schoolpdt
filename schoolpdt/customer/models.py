from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

    
class Customer(AbstractBaseUser):
    name=models.TextField(max_length=50)
    username=models.TextField(max_length=50)
    email=models.EmailField(max_length=100)
    number=models.TextField(max_length=20)
    #required
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    
    
    
    
    
    def __str__(self):
        return self.email
    

