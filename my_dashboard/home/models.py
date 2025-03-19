from django.db import models

# Create your models here.

class Records(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    alternative_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=250)
    dob = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=250)
    next_meet = models.DateField(null=True, blank=True)

