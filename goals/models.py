from django.contrib.auth import get_user_model
from django.db import models
from calendars.models import Sphere
from PIL import Image


User = get_user_model()


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
    sphere = models.ForeignKey(
        Sphere,
        on_delete=models.SET_NULL,
        related_name="my_goals",
        null=True,
    )
    date = models.DateField()
    done = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)
    description = models.TextField(max_length=200, blank=True)
    comment = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.text

    def save(self):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Mission(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="my_mission",
    )
    text = models.TextField(max_length=200)
