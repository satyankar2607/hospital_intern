from django.db import models

# Create your models here.
class doctor(models.Model):
    f_name = models.CharField(max_length=500)
    l_name = models.CharField(max_length=30)
    picture = models.ImageField(upload_to="photos/",null=True, blank=True)
    username = models.CharField(max_length=30)
    emailed = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    cnf_pwd = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

class patient(models.Model):
    f_name = models.CharField(max_length=500)
    l_name = models.CharField(max_length=30)
    picture = models.ImageField()
    username = models.CharField(max_length=30)
    emailed = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    cnf_pwd = models.CharField(max_length=30)
    address = models.CharField(max_length=30)