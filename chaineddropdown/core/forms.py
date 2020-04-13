from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Person, City, File, Teacher, Subject

# Form applied to create/delete file form.
# 1) Person Example
class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['country','city']
        widgets = {

            'country':forms.Select(attrs={  'class':'form-control mt-0',
                                            'style': 'font-size: 0.9rem'}),
            
            'city':forms.Select(attrs={  'class':'form-control mt-0',
                                         'style': 'font-size: 0.9rem'}),

        }
      
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
    

# 2) File Example    
class FileForm(forms.ModelForm):
    
    class Meta:
        model = File
        fields = ['subject','teacher']
        widgets = {

            'subject':forms.Select(attrs={  'class':'form-control mt-0',
                                            'style': 'font-size: 0.9rem'}),
            
            'teacher':forms.Select(attrs={  'class':'form-control mt-0',
                                         'style': 'font-size: 0.9rem'}),

        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].queryset = Teacher.objects.none()

        if 'subject' in self.data:
            try:
                subject_id = int(self.data.get('subject'))
                self.fields['teacher'].queryset = Teacher.objects.filter(teacher_subject_set=subject_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['teacher'].queryset = self.instance.subject.teacher.order_by('name')