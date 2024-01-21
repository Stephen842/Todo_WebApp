from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 200)
    details = models.TextField(null = True, blank = True)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title
