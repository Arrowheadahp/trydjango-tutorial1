from django.urls import path

from .views import (
    product_detail_view,
    product_create_view,
    product_delete_view,
    single_product_detail_view, 
    product_update_view,
)


app_name = 'product'

urlpatterns = [

    path('', product_detail_view),
    path('create/', product_create_view),
    path('<int:idp>/', single_product_detail_view, name= 'product_dynamic_view'),
    path('<int:idp>/delete/', product_delete_view, name= 'product_delete_view'),
    path('<int:idp>/update/', product_update_view, name= 'product_update_view'),

]