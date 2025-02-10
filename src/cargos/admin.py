from django.contrib import admin

from cargos.models import Cargo


class CargoAdmin(admin.ModelAdmin):
    list_display = ["title", "location", "destination", "weight", "status", "is_published"]
    list_filter = ["status", "is_published"]
    search_fields = ["title", "location", "destination"]


admin.site.register(Cargo, CargoAdmin)
