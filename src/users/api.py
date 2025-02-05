from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from addons.permissions.permission import RoleIsAdmin, IsObjectOwner
from users.serializers import UserSerializer


User = get_user_model()

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "user_id"

    def get_permissions(self):
        if self.action in ["list", "retrieve", "create"]:
            permission_classes = [AllowAny]

        if self.action in ["update", "partial_update"]:
            permission_classes = [RoleIsAdmin | IsObjectOwner]

        if self.action == "destroy":
            permission_classes = [RoleIsAdmin | IsObjectOwner]

        return [permission() for permission in permission_classes]


    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return User.objects.all()
        return User.objects.filter(id=user.id)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()

        if not user.is_active:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={"detail": "Not found."},
            )
        else:
            user.is_active = False
            user.save()

        return Response(
            {"detail": "User deactivated successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
