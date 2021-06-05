from django.urls import path

from .views import (
    list_view, 
    article_view,
    create_view, 
    delete_view, 
    edit_view,
    class_list_view,
    class_article_view,
    class_create_view,
    class_delete_view,
    class_edit_view
)

app_name = 'blog'
urlpatterns = [

    # path('',         list_view,     name= 'list_view'),
    # path('<int:id>/', article_view,  name= 'article_view'),
    # path('create/',  create_view,   name= 'create_view'),
    # path('<int:id>/delete/',  delete_view,   name= 'delete_view'),
    # path('<int:id>/edit/',    edit_view,     name= 'edit_view'),


    
    path('',         class_list_view.as_view(),     name= 'list_view'),
    path('<int:pk>/', class_article_view.as_view(),  name= 'article_view'),
    path('create/',  class_create_view.as_view(),   name= 'create_view'),
    path('<int:pk>/delete/',  class_delete_view.as_view(),   name= 'delete_view'),
    path('<int:pk>/edit/',    class_edit_view.as_view(),     name= 'edit_view'),

]