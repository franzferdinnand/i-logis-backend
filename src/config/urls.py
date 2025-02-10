
from django.contrib import admin
from django.urls import path, include

from config.settings import ROOT_API

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"{ROOT_API}/auth/", include("authentication.urls", "auth"),  name="auth"),
    path(f"{ROOT_API}/users/", include("users.urls", "users"),  name="users"),
    path(f"{ROOT_API}/cargos/", include("cargos.urls"),  name="cargos"),
    # path(f"{ROOT_API}/transports/", include("transports.urls"),  name="transports"),
]
