from django.shortcuts import render

# Create your views here.
from .models import product
from .forms import productform

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

def product_create_view(request):
    initial_data={
        'title': 'my initial title',
        'description': 'my initial description',
    }




    form = productform(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()


    
    context = {
        'form': form,
    }
    return render(request, 'product/create_product.html', context)