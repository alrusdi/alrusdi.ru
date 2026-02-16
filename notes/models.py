from django.db import models

class Group(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Группа заметок"
        verbose_name_plural = "Группы заметок"


class Note(models.Model):
    group = models.ForeignKey(Group, on_delete=models.RESTRICT)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_password = models.BooleanField(default=False)
    is_oneline = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"
