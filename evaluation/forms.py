from .models import Applicant
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class ApplicantForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))
    cc = forms.IntegerField(
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))
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
        self.fields['document'].widget.attrs.update({'type': 'file'})
        self.fields['document'].required = False