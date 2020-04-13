from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import City, Teacher
from .forms import PersonForm, FileForm

# Create your views here.
# 1) Person Example:
class PersonView(CreateView):
    template_name = "core/person_example.html"
    form_class = PersonForm


def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'core/dropdowncities.html', {'cities':cities})


# 2) File Example:
class FileView(CreateView):
    template_name = "core/file_example.html"
    form_class =  FileForm

def load_teachers(request):
    subject_id = request.GET.get('subject')
    teachers = Teacher.objects.filter(teacher_subject_set=subject_id).order_by('name')
    print(teachers)
    return render(request, 'core/dropdownteachers.html',{'teachers':teachers})
    
