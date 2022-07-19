from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, default="메롱", null=True, blank=True)
    view_auth = models.IntegerField(default=0, null=True, blank=True)
    color = models.CharField(max_length=10, default="#000000", null=True, blank=True)
    pup_date = models.DateTimeField(auto_now_add = True)


class Todo(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=20, null=True, blank=True)
    thumb_nail = models.ImageField(upload_to = 'todo/', null=True, blank=True)
    is_completed = models.BooleanField(default=False, null=True, blank=True)
    pup_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)