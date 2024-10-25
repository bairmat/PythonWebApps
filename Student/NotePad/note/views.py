from django.shortcuts import render

from django.views.generic import TemplateView
from markdown import markdown

from .models import Note, Superhero


class HeroListView(TemplateView):
    template_name = 'notes.html'

    def get_context_data(self, **kwargs):
        return {
            'object_list': Superhero.objects.all()
        }


class HeroDetailView(TemplateView):
    template_name = 'note.html'

    def get_context_data(self, **kwargs):
        return {
            'note': Superhero.objects.get(pk=kwargs['pk'])
        }
