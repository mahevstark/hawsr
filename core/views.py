from rest_framework import viewsets
from .models import User, Worker, Company, Building, Office, UserOffice
from .serializers import (UserSerializer, WorkerSerializer, CompanySerializer,
                          BuildingSerializer, OfficeSerializer, UserOfficeSerializer)
from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer

class UserOfficeViewSet(viewsets.ModelViewSet):
    queryset = UserOffice.objects.all()
    serializer_class = UserOfficeSerializer

class AdminLoginViewSet(viewsets.ViewSet):
    def create(self, request):
        # Extract the username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Perform authentication
        user = authenticate(username=username, password=password)

        if user is not None and (user.is_staff or user.is_superuser):
            # If authentication is successful and the user is an admin, return a success response
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'message': 'Admin login successful'
            }, status=status.HTTP_200_OK)
        else:
            # If authentication fails or the user is not an admin, return an error response
            return Response({'error': 'Invalid credentials or not an admin'}, status=status.HTTP_401_UNAUTHORIZED)

    # def get_permissions(self):
    #     # Only allow POST requests for admin login
    #     if self.action == 'create':
    #         return [permissions.AllowAny()]
    #     return super().get_permissions()
