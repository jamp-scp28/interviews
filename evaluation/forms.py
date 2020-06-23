from .models import Applicant
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('name','cc','document')
        labels = {
            'name': 'Nombre Completo',
            'cc':'No. Documento Identidad',
            'document': 'Evaluación'
        }
        
    def __init__(self, *args, **kwargs):
        super(ApplicantForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['cc'].widget.attrs.update({'class': 'form-control'})
        self.fields['document'].widget.attrs.update({'type': 'file'})