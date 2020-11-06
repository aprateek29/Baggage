from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/', null=True)
    rating = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def get_rating(self):
        return self.rating

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.email