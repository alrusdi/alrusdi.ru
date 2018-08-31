from django.db import models

# Create your models here.


class Page(models.Model):
    title = models.CharField(
        max_length=250
    )

    slug = models.SlugField(
        max_length=250,
    )

    content = models.TextField(
        blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
