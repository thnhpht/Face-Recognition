from django.db import models

# Create your models here.

class Attendance(models.Model):
    name = models.CharField(max_length=50)
    time = models.TimeField()

