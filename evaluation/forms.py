from .models import Applicant, appTest
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

class appTestForm(forms.ModelForm):
    class Meta:
        model = appTest
        fields = ('apprentice','question1','question2','question3','question4','question5','question6',)
        labels = {
            'apprentice': 'Aprendiz',
            'question1': 'Pregunta 1',
            'question2': 'Pregunta 2',
            'question3': 'Pregunta 3',
            'question4': 'Pregunta 4',
            'question5': 'Pregunta 5',
            'question6': 'Pregunta 6'
        }
    def __init__(self,*args, **kwargs):
        super(appTestForm, self).__init__(*args, **kwargs)
        self.fields['apprentice'].widget.attrs.update({'class': 'form-dropdown', 'id':'selectemp'})
        #self.fields['question1'].widget.attrs.update({'class': 'form-control'})