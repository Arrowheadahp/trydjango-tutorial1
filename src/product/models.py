from django.db import models

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=144)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=24)
    available = models.BooleanField(default=True)