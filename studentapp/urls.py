from django.urls import path
from studentapp.views import *

urlpatterns = [path("student-list/", student_list, name="student_list")]
