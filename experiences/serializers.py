from rest_framework.serializers import ModelSerializer

from .models import Perk, Experience


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"


class ExperienceSerializer(ModelSerializer):
    perks = PerkSerializer(many=True,read_only=True)

    class Meta:
        model = Experience
        exclude = (
            "created_at",
            "updated_at",
        )
