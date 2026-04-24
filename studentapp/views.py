from rest_framework.decorators import api_view
from studentapp.serializers import *
from studentapp.models import *
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def student_list(request):
    student_data = StudentInfo.objects.all()
    serializer = StudentSerializer(student_data, many=True)
    return Response(
        {
            "success": True,
            "message": "Student List Successfuly GET",
            "data": serializer.data,
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
def add_student(request):
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Student ADD Successfuly POST",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response({"success": False, "message": serializer.errors})


@api_view(["GET"])
def student_view(request, id):
    try:
        data = StudentInfo.objects.get(id=id)
    except StudentInfo.DoesNotExist:
        return Response(
            {"success": False, "message": "Student Not Found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    serializer = StudentSerializer(data)
    return Response(
        {
            "success": True,
            "message": "Student find Successfuly GET",
            "data": serializer.data,
        },
        status=status.HTTP_200_OK,
    )


@api_view(["PUT"])
def student_edit(request, id):
    try:
        data = StudentInfo.objects.get(id=id)
    except StudentInfo.DoesNotExist:
        return Response(
            {"success": False, "message": "Student Not Found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if request.method == "PUT":
        serializer = StudentSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Student Edit Successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {"Success": False, "message": "Student Edit Unsuccessfull"},
            status=status.HTTP_404_NOT_FOUND,
        )


@api_view(["DELETE"])
def student_delete(request, id):
    try:
        data = StudentInfo.objects.get(id=id)
    except StudentInfo.DoesNotExist:
        return Response(
            {"success": False, "message": "Student Not Found"},
            status=status.HTTP_404_NOT_FOUND,
        )
    data.delete()
    return Response(
        {
            "Success": True,
            "Message": "Student Data Deleted Succesfully",
        }
    )
