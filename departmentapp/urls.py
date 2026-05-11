from django.urls import path,include
from departmentapp.views import *
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'department',DepartmentModelViewSet,basename='department')

urlpatterns = [
    path('',include(router.urls))
]