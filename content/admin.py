from django.contrib import admin
from content.models import Page


@admin.decorators.register(Page)
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
