from django.shortcuts import render
from .forms import ApplicantForm
from .models import Applicant

from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.forms.models import model_to_dict
from django.db.models import Sum, Count
from django.core.files.storage import FileSystemStorage

@login_required(login_url="/login/")
def appl_list(request):
    if request.user.is_superuser:
        qs = Applicant.objects.all()
    else:
        qs = Applicant.objects.filter(interviewer=request.user)
    context = {'addint_list': qs}
    return render(request, "applicant_list.html", context)


@login_required(login_url="/login/")
def appl_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ApplicantForm()
        else:
            addint = Applicant.objects.get(pk=id)
            form = ApplicantForm(instance=addint)
        return render(request, "addint_form.html", {'form': form})
    else:
        if id == 0:
            form = ApplicantForm(request.POST, request.FILES)
        else:
            medicalexam = Applicant.objects.get(pk=id)
            
            form = ApplicantForm(request.POST, request.FILES, instance= medicalexam)

        if form.is_valid():
            form.save()
        return redirect('/')
    # else:
    #     if id == 0:
    #         form = ApplicantForm(request.POST, request.FILES)
    #     else:
    #         addint = Applicant.objects.get(pk=id)
    #         upload_file = request.FILES['document']
    #         fs = FileSystemStorage()
    #         fs.save(upload_file.name,upload_file)
    #         form = ApplicantForm(request.POST,request.FILES, instance= addint)
    #     #if form.is_valid():
    #         form.save()
    #     return redirect('/')
    #     #else:
    #     #    return render(request,"applicantForm.html",{'form':form})
