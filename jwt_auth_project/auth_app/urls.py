from django.urls import path,include
from auth_app.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register(r'student',StudentView,basename='student')
urlpatterns = [
    path('',include(router.urls)),
    path('register/',RegisterView.as_view(),name='RegisterView'),
    path('login/',LoginView.as_view(),name='LoginView'),
    path('logout/',LogoutView.as_view(),name='LogoutView'),

    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh')
    
]