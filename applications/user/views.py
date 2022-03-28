from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from applications.user.models import Profile
from applications.user.permissions import IsProfileAuthor
from applications.user.serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework import status, generics


class RegisterView(APIView):
    def post(self, request):
        data = request.data  # хранит то, что отправляет юзер
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully registered!', status=status.HTTP_201_CREATED)

class ActivationView(APIView):
    def get(self, request, activation_code):
        User = get_user_model()
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Your account was activated successfully', status=status.HTTP_200_OK)

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('Successfully logged out', status=status.HTTP_200_OK)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        user = request.user
        profile = Profile.objects.get(user=user.id)
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileUpdateView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsProfileAuthor]

