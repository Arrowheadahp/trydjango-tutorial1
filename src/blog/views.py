from django.shortcuts import render

# Create your views here.


from .models import article
from .forms import aform

from django.shortcuts import get_object_or_404

def list_view(requests):
    obj_list = article.objects.all()
    context = {
        'obj_list': obj_list,
    }

    return render(requests, 'article/list_view.html', context)


def article_view(requests, id):
    obj = get_object_or_404(article, id=id)
    context = {
        'obj': obj,
    }

    return render(requests, 'article/article_view.html', context)


def delete_view(requests, id):
    obj = get_object_or_404(article, id=id)
    context = {
        'obj': obj,
    }

    return render(requests, 'article/delete_view.html', context)







def create_view(requests):
    form = aform(requests.POST or None)
    context = {
        'form': form,
    }

    return render(requests, 'article/create_view.html', context)


def edit_view(requests, id):
    obj = get_object_or_404(article, id=id)
    form = aform(requests.POST or None, instance=obj)
    context = {
        'form': form,
    }

    return render(requests, 'article/create_view.html', context)
