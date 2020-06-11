from django.db import models
from employee.models import Employee

# Create your models here.
class AddInt(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    dated = models.DateTimeField(null=True, blank=True)
    interviewed = models.BooleanField()
    hire = models.BooleanField()

    def __str__(self):
        return self.employee.fullname