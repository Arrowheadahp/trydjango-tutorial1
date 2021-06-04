from django.urls import path

from .views import *

app_name = 'blog'
urlpatterns = [

    path('',         list_view,     name= 'list_view'),
    path('article/', article_view,  name= 'article_view'),
    path('create/',  create_view,   name= 'create_view'),
    path('delete/',  delete_view,   name= 'delete_view'),
    path('edit/',    edit_view,     name= 'edit_view'),

]