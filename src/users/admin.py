from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone_number" ,"role", "is_active"]
    list_filter = ["role", "is_active"]
    search_fields = ["email", "first_name", "last_name", "phone_number"]


admin.site.register(User, UserAdmin)
