from django.shortcuts import render
from django.views.generic import TemplateView

from content.models import Page


class IndexView(TemplateView):
    template_name = "content/index.html"

    def get_context_data(self, **kwargs):
        page = Page.objects.get(slug="index")
        return {
            "page": page
        }