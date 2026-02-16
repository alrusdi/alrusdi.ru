from django.contrib import admin
from notes.models import Group, Note


@admin.decorators.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.decorators.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "group", "is_password", "is_oneline", "created_at", "updated_at")
