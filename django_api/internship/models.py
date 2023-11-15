from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Internship(models.Model):
   
    internship_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    application_deadline = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()  
    is_paid = models.BooleanField(default=False)
    stipend = models.IntegerField(default=0)
    contact_email = models.EmailField(default='user012@example.com')

    def __str__(self):
        return self.internship_name
    
    
class ApplyIntern(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    intern_id = models.ForeignKey(Internship, on_delete=models.CASCADE)
    Graduation_name = models.CharField(max_length=255)
    year_of_study = models.IntegerField(default=1)
    cover_letter = models.TextField()
    skills = models.TextField()
    # resume = models.FileField(upload_to='uploads/')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Graduation_name
    


    
