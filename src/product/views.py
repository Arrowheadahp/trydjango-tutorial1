from django.shortcuts import render

# Create your views here.
from .models import product

def single_product_detail_view(request, idp):

    prd = product.objects.get(id=idp)
    context = {
        # 'title': prd.title,
        # 'price': prd.price,
        # 'description': prd.description,
        # 'available': prd.available,
        'prd':  prd,
    }

    return render(request, 'product/detail.html', context)


def product_detail_view(request):
    idp = 1
    return single_product_detail_view(request, idp)