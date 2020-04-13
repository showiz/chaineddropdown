from django.contrib import admin
from .models import Country, City, Subject, Teacher
# Register your models here.

# 1) Person Example
class CountryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Country, CountryAdmin)

class CityAdmin(admin.ModelAdmin):
    pass
admin.site.register(City, CityAdmin)

#--------

# 2) File Example
class SubjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subject, SubjectAdmin)

class TeacherAdmin(admin.ModelAdmin):
    pass
admin.site.register(Teacher, TeacherAdmin)