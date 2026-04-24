from django.urls import path
from studentapp.views import *

urlpatterns = [
    path("student-list/", student_list, name="student_list"),
    path("student-list/<int:id>/", student_view, name="student_view"),
    path("student-edit/<int:id>/", student_edit, name="student_edit"),
    path("student-delete/<int:id>/", student_delete, name="student_delete"),
    path("student-add/", add_student, name="add_student"),
]
