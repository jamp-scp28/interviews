from django.contrib import admin

# Register your models here.
from .models import Employee
from .models import Department
from .models import JobName

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(JobName)
