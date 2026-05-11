
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('studentapp.urls')),
    path('api/', include('teacherapp.urls')),
    path('api/', include('departmentapp.urls')),
]
