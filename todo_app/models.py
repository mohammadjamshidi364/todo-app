from django.db import models

from accounts.models import User



class TodoItem(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    label = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    completed_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.label