from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    year = models.IntegerField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
