from django.db import models

class Home(models.Model):
    frist_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=100)
    
# Create your models here.
