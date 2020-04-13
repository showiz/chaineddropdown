from django.db import models

# Create your models here.

#--------------------------------------1)_PERSON EXAMPLE_-------------------------------------------
class Country(models.Model):
    name = models.CharField(verbose_name="Name Country", max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(verbose_name="Name City", max_length=100)

    # Foreign Keys
    country = models.ForeignKey(Country, verbose_name="Country Name",on_delete=models.CASCADE, null=True)

class Person(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.country

#--------------------------------------2)_FILE EXAMPLE_-------------------------------------------
class Teacher(models.Model):
    name = models.CharField(verbose_name="Name Teacher", max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(verbose_name="Name Subject", max_length=100)

    # ManyToManyField
    teacher = models.ManyToManyField(Teacher, related_name = 'teacher_subject_set')

    def __str__(self):
        return self.name

class File(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject