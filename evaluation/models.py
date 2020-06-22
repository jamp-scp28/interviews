from django.db import models

# Create your models here.


class Applicant(models.Model):
    name = models.CharField(max_length=100,null=True)
    cc = models.IntegerField(null=True,blank=True)
    document = models.FileField(null=True,blank=True)