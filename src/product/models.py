from django.db import models


from django.urls import reverse

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=144)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=24)
    available = models.BooleanField(default=False)


    def get_absolute_url(self):     # This is to get the urls of each object that is created  
                                    # with this class


        # return (f'/product/{self.id}')

        return reverse('product:product_dynamic_view', kwargs={'idp': self.id})

    
    def get_delete_url(self):
        return reverse('product:product_delete_view', kwargs={'idp': self.id})

    
    
    def get_update_url(self):
        return reverse('product:product_update_view', kwargs={'idp': self.id})

