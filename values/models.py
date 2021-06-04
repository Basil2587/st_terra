from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.base import Model

User = get_user_model()


class ValueType(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class AlgorithmType(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Value(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="values",
    )
    title = models.CharField(max_length=200)
    type = models.ForeignKey(
        ValueType,
        on_delete=models.SET_NULL,
        related_name="values",
        null=True,
    )


class Algorithm(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="algorithms",
    )
    title = models.CharField(max_length=200)
    type = models.ForeignKey(
        AlgorithmType,
        on_delete=models.SET_NULL,
        related_name="algorithms",
        null=True,
    )
