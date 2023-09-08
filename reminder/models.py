from django.db import models

# Create your models here.
class Reminder(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    date = models.DateTimeField()