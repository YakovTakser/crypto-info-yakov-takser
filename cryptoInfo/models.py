from datetime import datetime

from django.db import models


# Create your models here.

class Crypto(models.Model):
    """Crypto Article Object"""

    name = models.CharField(max_length=300, null=False, blank=False)
    author = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=1000, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=400, null=True, blank=True)
    urlToImage = models.URLField(max_length=400, null=True, blank=True)
    publishedAt = models.DateTimeField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
