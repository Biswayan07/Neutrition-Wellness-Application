from django.db import models
from django.contrib.auth.models import User

class food(models.Model):
    name = models.CharField(max_length=200)
    calorie=models.DecimalField(max_digits=5,decimal_places=2,default=0,blank=True)

    def __str__(self):
        return str(self.name)

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.name)