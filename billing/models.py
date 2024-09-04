from django.db import models
from genuser.models import CustomUser
from datetime import date

# Create your models here.

class prevBill(models.Model):
    userInfo=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    meterusage= models.IntegerField()
    month=models.CharField(max_length=50)
    # year=models.IntegerField()
    readDate=models.DateField(default=date.today)
    dueDate=models.DateField(default=date.today)
    sanitaryCharge=models.IntegerField()
    meterCharge=models.DecimalField(max_digits=6,decimal_places=2,default=1)
    waterValue=models.DecimalField(max_digits=6,decimal_places=2)
    totalamount=models.DecimalField(max_digits=6,decimal_places=2)
    currentDue=models.DecimalField(max_digits=12,decimal_places=2,default=0)

    def __str__(self):
        return f"{self.userInfo.username}-{self.readDate}"


class waterCharge(models.Model):
    lessOrMore=models.CharField(max_length=40,default="")
    lessThanLiters=models.IntegerField()
    priceFOrLiters=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.lessOrMore

   


class tax(models.Model):

    taxName=models.CharField(max_length=50,default="")
    meterFee=models.DecimalField(max_digits=6,decimal_places=2)
    sanitaryCharges=models.IntegerField()
    duesInterest=models.IntegerField()
    otherCharges=models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.taxName

    

class dummy(models.Model):
    useid=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name=models.CharField(max_length=60)
    charge=models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    
