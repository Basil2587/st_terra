from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Target(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="targets",
    )
    title = models.CharField(max_length=100)
    done = models.BooleanField()
    date = models.DateField()


class Plan(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="plans",
    )
    title = models.CharField(max_length=100)
    done = models.BooleanField()
    date = models.DateField()


class Diary(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="diaries",
    )
    conclusion = models.CharField(max_length=200)
    achievements = models.CharField(max_length=200)
    good_things = models.CharField(max_length=200)
    date = models.DateField()
