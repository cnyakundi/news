from django.db import models
from django.utils import timezone


class Post(models.Model):
    url = models.CharField(max_length=250, unique=True)

    title = models.CharField(max_length=250)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    class Admin:
        pass
