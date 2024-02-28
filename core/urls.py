from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserViewSet, WorkerViewSet, CompanyViewSet, 
                    BuildingViewSet, OfficeViewSet, UserOfficeViewSet, AdminLoginViewSet)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'workers', WorkerViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'buildings', BuildingViewSet)
router.register(r'offices', OfficeViewSet)
router.register(r'user_offices', UserOfficeViewSet)

router.register(r'admin-login', AdminLoginViewSet, basename='admin-login')

urlpatterns = [
    path('', include(router.urls)),
]
