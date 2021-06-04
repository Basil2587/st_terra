from django.db.models import fields
from rest_framework import serializers
from results.models import Target, Plan, Diary
from lists.models import MyList, ListType
from values.models import Value, Algorithm, ValueType, AlgorithmType
from goals.models import GoalType, MyGoals


class TargetSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = "__all__"
        model = Target


class PlanSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = "__all__"
        model = Plan


class DiarySerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = "__all__"
        model = Diary


class ListTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ListType


class ListTypeField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = ListTypeSerializer(value)
        return serializer.data


class ListSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    type = ListTypeField(
        slug_field='id',
        queryset=ListType.objects.all(),
        required=False
    )

    class Meta:
        fields = "__all__"
        model = MyList



class ValueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ValueType


class ValueTypeField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = ValueTypeSerializer(value)
        return serializer.data

class ValueSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    type = ValueTypeField(
        slug_field='id',
        queryset=ValueType.objects.all(),
        required=False
    )

    class Meta:
        fields = "__all__"
        model = Value


class AlgorithmTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = AlgorithmType


class AlgorithmTypeField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = AlgorithmTypeSerializer(value)
        return serializer.data


class AlgorithmSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    type = AlgorithmTypeField(
        slug_field='id',
        queryset=AlgorithmType.objects.all(),
        required=False
    )

    class Meta:
        fields = "__all__"
        model = Algorithm


class GoalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = GoalType


class GoalTypeField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = GoalTypeSerializer(value)
        return serializer.data


class GoalSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    type = GoalTypeField(
        slug_field='id',
        queryset=GoalType.objects.all(),
        required=False
    )

    class Meta:
        fields = "__all__"
        model = MyGoals
