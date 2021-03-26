from django.db import models

# Create your models here.

class Prodaft(models.Model):
    Id = models.IntegerField()
    Name = models.CharField(max_length=70, blank=False, default='')
    Email = models.CharField(max_length=200,blank=False, default='')
    Phone = models.BooleanField(default=False)
    City = models.CharField(max_length=70, blank=False, default='')
    
    
