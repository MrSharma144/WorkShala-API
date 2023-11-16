from django.db import models 
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class InternPreference(models.Model):
    work_status = models.CharField(max_length=20, choices=[('Available', 'Available'), ('Not Available', 'Not Available')])
    skills = ArrayField(
        models.CharField(max_length=50), blank=True, null=True,default=list,
        verbose_name='Skills'
        )