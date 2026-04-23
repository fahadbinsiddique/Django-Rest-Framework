from rest_framework.decorators import api_view
from studentapp.serializers import *
from studentapp.models import *
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def student_list(request):
    student_data= StudentInfo.objects.all()
    serializer= StudentSerializer(student_data,many=True)
    return Response(serializer,status=status.HTTP_200_OK)