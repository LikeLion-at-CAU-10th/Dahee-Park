from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    age = models.IntegerField(blank=True)
    phone = models.CharField(max_length=20, null=False, blank=False)