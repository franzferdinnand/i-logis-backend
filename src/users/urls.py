from rest_framework.routers import DefaultRouter

from users.api import UserViewSet

app_name = "users"

router = DefaultRouter()
router.register("", UserViewSet)

urlpatterns = [] + router.urls