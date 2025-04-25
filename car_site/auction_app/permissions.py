from rest_framework import permissions

class CreateCar(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'seller':
            return True
        return False
