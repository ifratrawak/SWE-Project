from django.contrib.auth.models import User
from django.db import models

# Create your models here.
locations = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'),('Mohammadpur', 'Mohammadpur'),('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'),
             ('Uttara', 'Uttara'), ('Azimpur', 'Azimpur'), ('Khilkhet', 'Khilkhet'), ('Banani', 'Banani'),
             ('Nilkhet', 'Nilkhet'), ('Bashabo', 'Bashabo'), ('Rampura', 'Rampura'), ('Mouchak', 'Mouchak'),
             ('Mugdha', 'Mugdha'), ('Wari', 'Wari'), ('Shahabagh', 'Shahabagh')]

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(choices=locations, max_length=100)
    owner = models.OneToOneField(User, default=None, on_delete=models.CASCADE)


    def __str__(self):
        return self.name