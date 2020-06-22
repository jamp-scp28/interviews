from .models import Interview
from .forms import InterviewForm
from django.http import JsonResponse

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from employee.models import Employee
from django.forms.models import model_to_dict
from django.db.models import Sum, Count
from django.contrib.contenttypes.models import ContentType


# @login_required(login_url="/login/")
# class int_list(self, request):
#     """Generic class-based view listing books on loan to current user."""
#     model = Interview
#     template_name ='ui-tables-abs.html'
#     paginate_by = 10
    
#     def get_queryset(self):
#         return Interview.objects.filter(toUser=self.request.user)


@login_required(login_url="/login/")
def int_list(request):
    if request.user.is_superuser:
        created_by_user = Interview.objects.all()
    else:
        created_by_user = Interview.objects.filter(toUser=request.user)
    context = {'int_list': created_by_user}
    
    return render(request, "ui-tables-abs.html", context)


@login_required(login_url="/login/")
def int_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = InterviewForm()
        else:
            interview = Interview.objects.get(pk=id)
            employee_list = Employee.objects.all()
            form = InterviewForm(instance=interview)
            contextabs = {'form': form, 'employee_list': employee_list}
        return render(request, "abs_form.html", {'form': form, 'employee_list': Employee.objects.all()})
    else:
        if id == 0:
            form = InterviewForm(request.POST)
        else:
            interview = Interview.objects.get(pk=id)
            
            form = InterviewForm(request.POST,instance= interview)
        if form.is_valid():
            form.save()
            return redirect('/int_list')
        else:
            return render(request,"abs_form.html",{'form':form})

@login_required(login_url="/login/")
def int_delete(request,id):
    interview = Interview.objects.get(pk=id)
    interview.delete()
    return redirect('/int_list')