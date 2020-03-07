from django.views.generic import TemplateView
from auth.backend.decorators import view_allow_any


@view_allow_any()
class IndexView(TemplateView):
    template_name = 'index.html'
