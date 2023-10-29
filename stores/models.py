import datetime

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


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.EmailField(max_length=11)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30,blank=True, null=True)
    quantity = models.CharField(max_length=30, default=None)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='images/products/')

    def __str__(self):
        return self.name

# product orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.product.name + '-> ' + self.product.store.name