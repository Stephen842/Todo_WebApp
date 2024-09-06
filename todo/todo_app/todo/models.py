from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 250)
    details = models.TextField(null = True, blank = True)
    completed = models.BooleanField(default = False)
    date = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed']
