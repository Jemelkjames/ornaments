from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    distribution = models.TextField()  # Distribution details
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
