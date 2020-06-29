from django.db import models
from django.utils import timezone
from employee.models import Employee

class Applicant(models.Model):
    name = models.CharField(max_length=100,null=True)
    cc = models.IntegerField(null=True)
    document = models.FileField()
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

class appTest(models.Model):
    apprentice = models.ForeignKey(Employee, on_delete=models.CASCADE)
    question1 = models.BooleanField()
    question2 = models.BooleanField()
    question3 = models.BooleanField()
    question4 = models.BooleanField()
    question5 = models.BooleanField()
    question6 = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.apprentice.fullname