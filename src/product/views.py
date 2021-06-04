from django.shortcuts import render

# Create your views here.
from .models import product
from .forms import productform




from django.shortcuts import get_object_or_404
def single_product_detail_view(request, idp):

    # prd = product.objects.get(id=idp)
    prd = get_object_or_404(product, id=idp)    # to handle error when the product does not exist
    context = {
        # 'title': prd.title,
        # 'price': prd.price,
        # 'description': prd.description,
        # 'available': prd.available,
        'prd':  prd,
    }

    return render(request, 'product/detail.html', context)





def product_detail_view(request):
    # idp = 1
    # return single_product_detail_view(request, idp)

    queryset = product.objects.all() # returns list of all objects
    context = {
        'object_list': queryset
    }

    return render(request, 'product/product_list.html', context)

def product_create_view(request):
    initial_data={
        'title': 'my initial title',
        'description': 'my initial description',
    }




    form = productform(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        return redirect('../')


    
    context = {
        'form': form,
    }
    return render(request, 'product/create_product.html', context)



from django.shortcuts import redirect
def product_delete_view(request, idp):
    prd = get_object_or_404(product, id=idp)
    
    if request.method == 'POST':
        prd.delete()
        return redirect('../../')
    


    context = {
        'object': prd,
    }
    return render(request, 'product/product_delete.html', context)


def product_update_view(request, idp):
    prd = get_object_or_404(product, id=idp)
    form = productform(request.POST or None, instance=prd)

    if form.is_valid():
        form.save()
        return redirect('../')
    
    context = {
        'form': form 
    }

    return render(request, 'product/create_product.html', context)