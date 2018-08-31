from django.contrib import admin

# Register your models here.
from content.models import Page



@admin.decorators.register(Page)
class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
