from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ListType(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class MyList(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="lists",
    )
    title = models.CharField(max_length=100)
    type = models.ForeignKey(
        ListType,
        on_delete=models.SET_NULL,
        related_name="lists",
        null=True,
    )
    done = models.BooleanField()
    favorite = models.BooleanField()
