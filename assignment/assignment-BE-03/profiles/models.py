from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    age = models.IntegerField(blank=True)
    phone = models.CharField(max_length=20, null=False, blank=False)
    

class Class(models.Model):
    subject = models.CharField(max_length=50, null=False, blank=False)
    name = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True)
