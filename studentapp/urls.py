from django.urls import path
from studentapp.views import *

urlpatterns = [
    path("student-list/", student_list, name="student_list"),
    path("student-add/", add_student, name="add_student"),
    path("student-view/<int:id>/", student_view, name="student_view"),
]
