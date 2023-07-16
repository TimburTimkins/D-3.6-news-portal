from django.views.generic import ListView, DetailView
from .models import News


class NewsList(ListView):
    model = News
    ordering = '-date_on'
    template_name = 'default.html'
    context_object_name = 'text'

class NewsDetail(DetailView):
    model = News
    template_name = 'onenew.html'
    context_object_name = 'new'