from rest_framework import serializers

from users.models import User
from users.utils.password_validator import validate_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "role",
            "is_active",
            "is_staff",
            "is_superuser",
        ]
        read_only_fields = ["password", "confirm_password", "is_active", "is_staff", "is_superuser"]

    def create(self, validated_data):
        return User.objects.create(**validated_data)
