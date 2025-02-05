from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission

from users.utils.roles import Role


User = get_user_model()

def user_authenticated(user):
    if isinstance(user, AnonymousUser):
        raise PermissionDenied("Forbidden")


class RoleIsAdmin(BasePermission):
    def has_permission(self, request, view):
        user_authenticated(request.user)

        match(request.user.role == Role.ADMIN, request.user.is_staff):
            case(True, True):
                return True
            case(True, False):
                return True
            case _:
                return False

class RoleIsTransportOwner(BasePermission):
    def has_permission(self, request, view):
        user_authenticated(request.user)
        return request.user.role == Role.TRANSPORT_OWNER

class RoleIsCargoOwner(BasePermission):
    def has_permission(self, request, view):
        user_authenticated(request.user)
        return request.user.role == Role.CARGO_OWNER

class IsObjectOwner(BasePermission):
    def has_permission(self, request, view):
        user_authenticated(request.user)
        return request.user.id == view.get_object().user.id

    def has_object_permission(self, request, view, obj):
        return obj.id == request.user.id
