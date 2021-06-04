from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class GoalType(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class MyGoals(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="my_goals",
    )
    text = models.TextField()
    image = models.ImageField(
        upload_to="my_goals/", blank=True, verbose_name="Картинка"
    )
    type = models.ForeignKey(
        GoalType,
        on_delete=models.SET_NULL,
        related_name="my_goals",
        null=True,
    )
    date = models.DateField()

    def __str__(self):
        return self.text

