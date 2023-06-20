from django.db import models
from authentication.models import User

class Task(models.Model):
    
    TASK_STATUS_CHOICES = [
        ('ready', 'Ready'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]   
    title = models.CharField(max_length=300)
    due_date = models.DateField(null=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default = 'ready')
    description = models.CharField(max_length=1000, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
 
# Create your models here.
