from rest_framework.routers import DefaultRouter

from users.api import UserViewSet

router = DefaultRouter()
router.register("", UserViewSet)

urlpatterns = [] + router.urls