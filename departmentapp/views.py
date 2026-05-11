from departmentapp.serializers import *
from departmentapp.models import *
from rest_framework.viewsets import ModelViewSet 

# Create your views here.
class DepartmentModelViewSet(ModelViewSet):
    queryset = DepartmentModel.objects.all()
    serializer_class = departmentSerailizer