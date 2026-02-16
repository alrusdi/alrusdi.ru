from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from content.models import Page


class IndexView(TemplateView):
    template_name = "content/page.html"

    def get_context_data(self, **kwargs):
        page = get_object_or_404(Page, slug="index")
        return {
            "page": page
        }


class PageView(TemplateView):
    template_name = "content/page.html"

    def get_context_data(self, **kwargs):

        page = get_object_or_404(Page, slug=kwargs.get("slug"))

        if page.is_private and self.request.user.is_anonymous:
            raise Http404

        return {
            "page": page
        }
