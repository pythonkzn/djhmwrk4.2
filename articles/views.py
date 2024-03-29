from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    object_list = Article.objects.all().defer('published_at').select_related('author', 'genre')
    context = {'object_list': object_list}



    return render(request, template_name, context)
