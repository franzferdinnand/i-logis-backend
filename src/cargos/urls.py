from rest_framework.routers import DefaultRouter

from cargos.api import CargoViewSet


app_name = "cargos"

router = DefaultRouter()

router.register(r"", viewset=CargoViewSet, basename="cargos")

urlpatterns = [] + router.urls