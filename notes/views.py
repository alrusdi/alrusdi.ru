from django.http import Http404
from django.views.generic import TemplateView

from notes.models import Note

class NotesListView(TemplateView):
    template_name = "notes/list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        if self.request.user.is_anonymous:
            raise Http404

        ctx.update({
            "notes": Note.objects.order_by("-updated_at").prefetch_related("group")
        })
        return ctx
