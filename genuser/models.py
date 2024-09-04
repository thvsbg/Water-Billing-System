from django.db import models
from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class CustomUser(AbstractUser):
    
    address=models.CharField(max_length=300, default="")
    meternumber= models.IntegerField(unique=True, default=1)

    
    








    


