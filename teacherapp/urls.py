from django.urls import path
from teacherapp.views import *

urlpatterns = [
    path("teacher-list/",TeacherApiView.as_view(),name='TeacherApiView'),
    path("teacher-details/<int:id>/",TeacherDetailsApiView.as_view(),name='TeacherDetailsApiView')
]
