from rest_framework.permissions import BasePermission


class IsSuperAdmin(BasePermission):
    message = 'You must be the Super Admin'

    def has_permission(self, request, view):
        return request.user.is_superuser and request.user.role==1

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user