from django.db import models
from employee.models import Employee
from django.contrib.auth.models import User

class Interviewer(models.Model):
    name = models.CharField(null=True, blank=True,max_length=50,default="0")
    def __str__(self):
        return self.name
class Aca_level(models.Model):
    name = models.CharField(null=True, blank=True,max_length=50,default="0")
    def __str__(self):
        return self.name

class Job_afinity(models.Model):
    options = models.CharField(null=True, blank=True,max_length=50,default="0")
    def __str__(self):
        return self.options

class Apareance(models.Model):
    options = models.CharField(null=True, blank=True,max_length=50,default="0")
    def __str__(self):
        return self.options

class Responsability(models.Model):
    options = models.CharField(null=True, blank=True,max_length=50,default="0")
    def __str__(self):
        return self.options

class Aspirations(models.Model):
    options = models.CharField(null=True, blank=True,max_length=50,default="0")
    def __str__(self):
        return self.options

class Aca_concordance(models.Model):
    options = models.CharField(null=True, blank=True,max_length=50,default="0")
    def __str__(self):
        return self.options

class Puntuality(models.Model):
    options = models.CharField(null=True, blank=True,max_length=50,default="0")
    def __str__(self):
        return self.options

class Verbal_com(models.Model):
    options = models.CharField(null=True, blank=True,max_length=50,default="0")
    def __str__(self):
        return self.options

class Ove_result(models.Model):
    options = models.CharField(null=True, blank=True,max_length=50,default="0")
    def __str__(self):
        return self.options

class Recomendation(models.Model):
    options = models.CharField(null=True, blank=True,max_length=50,default="0")
    def __str__(self):
        return self.options

class Interview(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True,blank=True,)
    dated = models.DateTimeField(null=True, blank=True)
    interviewer = models.ForeignKey(Interviewer,on_delete=models.CASCADE,default=0)

    passport = models.BooleanField(default=False)
    dis_travel = models.BooleanField(default=False)
    visa = models.BooleanField(default=False)
    no_children = models.IntegerField(null=True, blank=True)
    w_live = models.CharField(null=True,blank=True,max_length=100)
    dis_inc = models.DateTimeField(null=True, blank=True)
    strenghts = models.CharField(null=True,blank=True,max_length=100)
    weakness = models.CharField(null=True,blank=True,max_length=100)
    int_rel = models.CharField(null=True,blank=True,max_length=100)
    team_work = models.CharField(null=True,blank=True,max_length=100)
    aca_level = models.ForeignKey(Aca_level,on_delete=models.CASCADE,default=0)
    job_afinity = models.ForeignKey(Job_afinity,on_delete=models.CASCADE,default=0)
    other_academy = models.CharField(null=True,blank=True,max_length=50)

    apareance = models.ForeignKey(Apareance,on_delete=models.CASCADE,default=0)
    responsability = models.ForeignKey(Responsability,on_delete=models.CASCADE,default=0)
    aspirations = models.ForeignKey(Aspirations,on_delete=models.CASCADE,default=0)

    aca_concordance = models.ForeignKey(Aca_concordance,on_delete=models.CASCADE,default=0)
    puntuality = models.ForeignKey(Puntuality,on_delete=models.CASCADE,default=0)
    verbal_com = models.ForeignKey(Verbal_com,on_delete=models.CASCADE,default=0)
    
    observations = models.CharField(null=True,blank=True,max_length=100)

    ove_result = models.ForeignKey(Ove_result,on_delete=models.CASCADE,default=0)
    recomendation = models.ForeignKey(Recomendation,on_delete=models.CASCADE,default=0)
    toUser = models.ForeignKey(User,on_delete=models.CASCADE,default=0)     
