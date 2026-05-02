from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from teacherapp.models import *
from teacherapp.serializers import *


class TeacherApiView(APIView):

    def get_object(self, id):
        try:
            return TeacherInfo.objects.get(id=id)
        except TeacherInfo.DoesNotExist:
            return Response(
                {
                    "success": "False",
                    "message": "teacher data not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

    def get(self, request, id=None):

        if not id:
            teacher_data = TeacherInfo.objects.all()
            serializer = TeacherSerializer(teacher_data, many=True)
            return Response(
                {
                    "success": "True",
                    "message": "teacher data GET Succesfully",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        else:

            teacher_data = self.get_object(id)

            serializer = TeacherSerializer(teacher_data)
            return Response(
                {
                    "success": "True",
                    "message": "teacher data single GET Succesfully",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": "True",
                    "message": "teacher data created POST Succesfully to database",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
    def put(self,request,id):
        teacher_data= self.get_object(id)
        if teacher_data:
            serializer = TeacherSerializer(teacher_data,data=request.data)
            if serializer.is_valid()
                serializer.save()
                return Response(
                {
                    "success": "True",
                    "message": "teacher data Update Succesfully ",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        def delete(self,request,id):
            


