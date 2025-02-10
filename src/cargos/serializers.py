from rest_framework import serializers


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = "cargos.Cargo"
        fields = [
            "id",
            "title",
            "description",
            "owner",
            "location",
            "destination",
            "weight",
            "status",
            "slug",
            "is_published",
            "created_at",
            "updated_at",

        ]
        read_only_fields = ["id", "owner", "created_at", "updated_at", "is_published", "slug"]
