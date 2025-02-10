from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from addons.permissions.permission import RoleIsAdmin, IsObjectOwner, RoleIsCargoOwner
from cargos.models import Cargo
from cargos.serializers import CargoSerializer


class CargoViewSet(ViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
    lookup_kwarg = "cargo_id"

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]

        if self.action in ["create"]:
            permission_classes = [RoleIsAdmin | IsObjectOwner | RoleIsCargoOwner]

        if self.action in ["update", "partial_update", "destroy"]:
            permission_classes = [RoleIsAdmin | IsObjectOwner]

        return [permission() for permission in permission_classes]
