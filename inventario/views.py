from django.shortcuts import render
from django.views import generic
from .models import Equipo

class EquipoListView(generic.ListView):
    model = Equipo
    paginate_by = 1
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(EquipoListView, self).get_context_data(**kwargs)
        context['current_page'] = context.pop('page_obj', None)
        return context


