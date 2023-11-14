from django.db import models

# Create your models here.

class Internship(models.Model):
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    application_deadline = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    stipend = models.IntegerField()