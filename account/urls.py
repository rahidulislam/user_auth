from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (CustomerRegisterView, StaffRegisterView,
                    SuperAdminRegisterView, ProfileUpdateView)

urlpatterns = [
    path('api/v1/customer/register/',
         CustomerRegisterView.as_view(), name='customer_register'),
    path('api/v1/staff/register/',
         StaffRegisterView.as_view(), name='staff_register'),
    path('api/v1/superadmin/register/',
         SuperAdminRegisterView.as_view(), name='superadmin_register'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/profile/<int:pk>/',
         ProfileUpdateView.as_view(), name='profile_update'),
]
