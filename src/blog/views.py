from django.shortcuts import render

# Create your views here.


from .models import article
from .forms import aform

from django.shortcuts import get_object_or_404
from django.urls import reverse






from django.views.generic import (
    CreateView, 
    DetailView, 
    DeleteView, 
    ListView, 
    UpdateView,
)

class class_list_view(ListView):
    template_name = 'article/list_view.html'
    queryset = article.objects.all()


class class_article_view(DetailView):
    template_name = 'article/article_view.html'
    queryset = article.objects.all()


class class_create_view(CreateView):
    template_name = 'article/create_view.html'
    form_class = aform
    queryset = article.objects.all()


class class_delete_view(DeleteView):
    template_name = 'article/delete_view.html'
    # success_url = reverse('blog:list_view')
    success_url = '../../'
    queryset = article.objects.all()


class class_edit_view(UpdateView):
    template_name = 'article/create_view.html'
    form_class = aform
    queryset = article.objects.all()








def list_view(requests):
    obj_list = article.objects.all()
    context = {
        'object_list': obj_list,
    }

    return render(requests, 'article/list_view.html', context)


def article_view(requests, pk):
    obj = get_object_or_404(article, id=pk)
    context = {
        'obj': obj,
    }

    return render(requests, 'article/article_view.html', context)


def delete_view(requests, pk):
    obj = get_object_or_404(article, id=pk)
    context = {
        'obj': obj,
    }

    return render(requests, 'article/delete_view.html', context)







def create_view(requests):
    form = aform(requests.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        form.save()

    return render(requests, 'article/create_view.html', context)


def edit_view(requests, pk):
    obj = get_object_or_404(article, id=pk)
    form = aform(requests.POST or None, instance=obj)
    context = {
        'form': form,
    }
    if form.is_valid():
        form.save()

    return render(requests, 'article/create_view.html', context)
