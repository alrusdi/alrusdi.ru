from django.db import models

from tinymce.models import HTMLField


class Page(models.Model):
    title = models.CharField(
        max_length=250
    )

    slug = models.SlugField(
        max_length=250,
    )

    content = HTMLField(
        blank=True, null=True
    )

    is_private = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
