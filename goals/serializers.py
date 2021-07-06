from rest_framework import serializers
from .models import *
from calendars.serializers import SphereField


class GoalSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    sphere = SphereField(
        slug_field='id',
        queryset=Sphere.objects.all(),
        required=False
    )

    class Meta:
        fields = "__all__"
        model = MyGoals


class MissionSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = "__all__"
        model = 