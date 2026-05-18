from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from auth_app.serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class= RegisterSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer= self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'success':True,
            'massage':'User SignUp Succesfully'
        },status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            "success": True,
            "message":'Logged in Successfully',
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "data": {
                "username": user.username,
                "email": user.email,
                "user_type": user.user_type
            }
        }, status=status.HTTP_200_OK)

class StudentView(ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    permission_classes=[IsAuthenticated]
    http_method_names=['get','post']

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()  

            return Response({
                "success": True,
                "message": "Logout successful"
            })
        except Exception as e:
            return Response({
                "success": False,
                "message": "Invalid refresh token"
            }, status=status.HTTP_400_BAD_REQUEST)