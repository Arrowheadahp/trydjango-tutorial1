from django.db import models

# Create your models here.

from django.urls import reverse


class article(models.Model):
    title   = models.CharField(max_length=120)
    content = models.TextField()
    active  = models.BooleanField(default=True)
    

    def get_absolute_url(self):
        return reverse('blog:article_view', kwargs={'pk': self.id})
        
    def get_edit_url(self):
        return reverse('blog:edit_view', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('blog:delete_view', kwargs={'pk': self.id})

    def get_create_url(self):
        return reverse('blog:create_view')

    def get_list_url(self):
        return reverse('blog:list_view')