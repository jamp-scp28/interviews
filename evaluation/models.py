from django.db import models
from django.utils import timezone
# Create your models here.


class Applicant(models.Model):
    name = models.CharField(max_length=100,null=True)
    cc = models.IntegerField(null=True)
    document = models.FileField()
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name