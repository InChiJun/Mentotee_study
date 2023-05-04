from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Bookmark
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkListView(ListView):
    model = Bookmark