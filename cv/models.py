from django.conf import settings
from django.db import models
from django.utils import timezone

class CV(models.Model):
    title = models.CharField(max_length=200)
    profile = models.TextField()
    career = models.TextField()
    skills = models.TextField()

    def save(self):
        self.save()