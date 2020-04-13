from django.urls import path
from .views import PersonView, FileView
from .views import load_cities, load_teachers

urlpatterns = [
    # 1) Person Example
    path('', PersonView.as_view(), name='person_example'),
    path('ajax/load-cities',load_cities, name="ajax_load_cities"),

    # 2) File Example
    path('file_example/', FileView.as_view(), name='file_example'),
    path('ajax/load-teachers',load_teachers, name="ajax_load_teachers"),

]