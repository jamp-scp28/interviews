from .models import Interview
from django import forms
from django.core.validators import RegexValidator

class InterviewForm(forms.ModelForm):
    no_children = forms.CharField(
        label = "No. de Hijos (Si Aplica)",
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        )
    )
    w_live = forms.CharField(
        label = "Personas con las que vive",
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))
    strenghts = forms.CharField(
        label = "Fortalezas",
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))
    weakness = forms.CharField(
        label = "Debilidades",
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))
    int_rel = forms.CharField(
        label = "Relaciones Interpersonales",
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))
    team_work = forms.CharField(
        label = "Trabajo en Equipo",
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))
    other_academy = forms.CharField(
        label = "Otros Estudios",
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))
    observations = forms.CharField(
        label = "Observaciones del Entrevistador",
        widget=forms.TextInput(
            attrs={  
                "class": "form-control"
            }
        ))
    class Meta:
        model = Interview
        fields = '__all__'
        labels = {
            'employee':'Aspirante',
            'dated':'Fecha Entrevista',
            'hour':'Hora Entrevista',
            'interviewer':'Entrevistador',
            'passport':'Tiene Pasaporte?',
            'dis_travel':'Tiene Disponibilidad para viajar?',
            'visa':'Tiene Visa?',
            'no_children':'No. de Hijos (Si aplica)',
            'w_live':'Con quien vive?',
            'dis_inc':'Fecha de Disponibilidad?',
            'strenghts':'Fortalezas',
            'weakness':'Debilidades',
            'int_rel':'Relaciones Interpersonales',
            'team_work':'Trabajo en Equipo',
            'aca_level':'Nivel Academico',
            'job_afinity':'Afinidad del Trabajo con el Estudio',
            'other_academy':'Tiene otros estudios?',
            'passport':'Tiene Pasaporte?',
            'apareance':'APARIENCIA PERSONAL (voz,tono,modales,expresión, temperamento teniendo en cuenta características del cargo)',
            'responsability':'RESPONSABILIDAD (Motivos para dejar trabajos, gradode compromiso con lo que emprende)',
            'aspirations':'CALIDAD DE SUS ASPIRACIONES Y OBJETIVOS PERSONALES',
            'aca_concordance':'CONCORDANCIA CON EL PERFIL (Cumple con las especificaciones del cargo)',
            'puntuality':'Puntualidad',
            'verbal_com':'Comunicacion',
            'observations':'Comentarios',
            'ove_result':'Calificacion General',
            'recomendation':'Recomendacion',  
        }

    def __init__(self, *args, **kwargs):
        super(InterviewForm, self).__init__(*args, **kwargs)
        #self.fields['days'].validators = [RegexValidator(r'^[\d]{1,3}$', message="Value must be an integer and less than 3 numbers long")]
        # self.fields['leaveconcept'].empty_label = "Select"
        # self.fields['leaveconcept'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['dated'].widget.attrs.update({'class': 'form-control','id':'datepicker'})
        self.fields['dated'].input_formats=['%Y-%m-%d %H:%M:%S']
        #self.fields['dated'].format=['%Y/%m/%d %H:%M']
        self.fields['dis_inc'].widget.attrs.update({'class': 'form-control','id':'datepicker2'})
        self.fields['dis_inc'].input_formats=['%Y-%m-%d %H:%M:%S']
        #self.fields['dis_inc'].input_formats=['%Y/%m/%d %H:%M']
        self.fields['employee'].empty_label = "Select"
        self.fields['employee'].widget.attrs.update({'class': 'form-dropdown', 'id':'selectemp'})
        self.fields['interviewer'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['aca_level'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['job_afinity'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['apareance'].widget.attrs.update({'class': 'form-dropdown'}) 
        self.fields['responsability'].widget.attrs.update({'class': 'form-dropdown'}) 
        self.fields['aspirations'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['aca_concordance'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['puntuality'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['verbal_com'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['ove_result'].widget.attrs.update({'class': 'form-dropdown'})
        self.fields['recomendation'].widget.attrs.update({'class': 'form-dropdown'})