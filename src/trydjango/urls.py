"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, contact_view, about_view
# from product.views import (
#     product_detail_view,
#     product_create_view,
#     product_delete_view,
#     single_product_detail_view, 
#     product_update_view,
# )

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view, name= 'home'),
    path('contact/', contact_view),
    path('about/', about_view),



    # path('product/', product_detail_view),
    # path('create/', product_create_view),
    # path('product/<int:idp>/', single_product_detail_view, name= 'product_dynamic_view'),
    # path('product/<int:idp>/delete/', product_delete_view, name= 'product_delete_view'),
    # path('product/<int:idp>/update/', product_update_view, name= 'product_update_view'),


    ### we can do this in product/urls.py
    path('product/', include('product.urls')),

    path('blog/', include('blog.urls')),
]
