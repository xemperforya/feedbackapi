from django.db import models
from django.db.models.base import Model

class feedback(models.Model):
    email = models.EmailField(unique=True)
    feed = models.TextField(default="")
    tag = models.BooleanField(default=True)
    feed_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feed
    