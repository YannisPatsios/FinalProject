# Create your models here.
from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/properties')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
