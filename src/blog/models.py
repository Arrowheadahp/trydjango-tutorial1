from django.db import models

# Create your models here.

from django.urls import reverse


class article(models.Model):
    title   = models.CharField(max_length=120)
    content = models.TextField()
    active  = models.BooleanField(default=True)
    

    def get_original_url(self):
        return reverse('blog:article_view', 'article_view')
        
    def get_edit_url(self):
        return reverse('blog:article_view', 'edit_view')

    def get_delete_url(self):
        return reverse('blog:article_view', 'delete_view')

    def get_create_url(self):
        return reverse('blog:article_view', 'create_view')

    def get_list_url(self):
        return reverse('blog:article_view', 'list_view')