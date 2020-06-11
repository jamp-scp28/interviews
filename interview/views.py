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

@login_required(login_url="/login/")
def int_list(request):
    # labels = []
    # data = []
    # data2 = []
    #abs_data = Interview.objects.values('leaveconcept__leaveconcept').annotate(Sum('days'))
    #abs_data2 = Interview.objects.values('leaveconcept__leaveconcept').annotate(Count('employee'))
    # print(abs_data)
    # print(abs_data2)

    # for abs in abs_data:
    #     labels.append(abs['leaveconcept__leaveconcept'])
    #     data.append(abs['days__sum'])

    # for abs2 in abs_data2:
    #     data2.append(abs2['employee__count'])


    context = {'int_list': Interview.objects.all()}
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