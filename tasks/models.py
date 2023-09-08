from django.db import models

# Create your models here.
class Task(models.Model):
    tilte = models.CharField(max_length=200,null=True,blank=True)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.tilte