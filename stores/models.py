from django.contrib.auth.models import User
from django.db import models

# Create your models here.
locations = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Mohammadpur', 'Mohammadpur'),
             ('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'),
             ('Uttara', 'Uttara'), ('Azimpur', 'Azimpur'), ('Khilkhet', 'Khilkhet'), ('Banani', 'Banani'),
             ('Nilkhet', 'Nilkhet'), ('Bashabo', 'Bashabo'), ('Rampura', 'Rampura'), ('Mouchak', 'Mouchak'),
             ('Mugdha', 'Mugdha'), ('Wari', 'Wari'), ('Shahabagh', 'Shahabagh')]


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(choices=locations, max_length=100)
    owner = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    store_img = models.ImageField(upload_to="images/stores/", null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.EmailField(max_length=11)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='images/products/')

    def __str__(self):
        return self.name


