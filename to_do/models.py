from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.

class Task (models.Model) :
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=200, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title