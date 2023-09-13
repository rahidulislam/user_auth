# from django.contrib.auth import authenticate
# from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
# from rest_framework.authtoken.models import Token
# from rest_framework.generics import get_object_or_404, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

# from account.models import User, Profile
from account.serializers import CustomerSerializer
# from hotel_motel_project.permissions import IsCustomer


# # Create your views here.

# Customer Sign Up
# class CustomerSignUpAPIView(APIView):
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save(role=3)
#             return Response(serializer.data, status.HTTP_200_OK)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class CustomerSignupAPI(APIView):
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

# # Vendor Sign Up
# class VendorSignUpAPIView(APIView):
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save(role=2)
#             return Response(serializer.data, status.HTTP_200_OK)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# # All User Sign In
# class SignInAPIView(APIView):
#     serializer_class = SignInSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data.get('email')
#             password = serializer.validated_data.get('password')
#             if User.objects.filter(email=email).exists():
#                 user = authenticate(request, email=email, password=password)
#                 if user:
#                     token, created = Token.objects.get_or_create(user=user)
#                     data = {
#                         "id": user.id,
#                         "fullname": user.get_full_name(),
#                         "token": token.key,
#                         "role": user.get_role_display()
#                     }
#                     return Response(data, status.HTTP_200_OK)
#                 return Response({"detail": "wrong Credential"}, status.HTTP_400_BAD_REQUEST)
#             return Response({"detail": "User does not Found"}, status.HTTP_404_NOT_FOUND)
#         return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


# # All User Sign Up
# class SignOutAPIView(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def post(self, request):
#         request.user.auth_token.delete()
#         return Response(status.HTTP_200_OK)


# class UserProfileRetrieveView(RetrieveUpdateAPIView):
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     http_method_names = ['patch', 'get']

#     def get_object(self):
#         return get_object_or_404(Profile, user=self.request.user)

#     def perform_update(self, serializer):
#         instance = self.get_object()
#         first_name = self.request.data.get('first_name', None)
#         last_name = self.request.data.get('last_name', None)
#         updated_instance = serializer.save(user=instance.user)
#         if first_name:
#             updated_instance.user.first_name = first_name
#             updated_instance.user.save()
#         if last_name:
#             updated_instance.user.last_name = last_name
#             updated_instance.user.save()