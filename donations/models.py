from django.db import models
from django.contrib.auth.models import User

# Create your models here.

locations = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'),('Mohammadpur', 'Mohammadpur'),('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'),
             ('Uttara', 'Uttara'), ('Azimpur', 'Azimpur'), ('Khilkhet', 'Khilkhet'), ('Banani', 'Banani'),
             ('Nilkhet', 'Nilkhet'), ('Bashabo', 'Bashabo'), ('Rampura', 'Rampura'), ('Mouchak', 'Mouchak'),
             ('Mugdha', 'Mugdha'), ('Wari', 'Wari'), ('Shahabagh', 'Shahabagh')]

sex = [('Male','Male'), ('Female', 'Female')]

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    location = models.CharField(choices=locations, max_length=100)
    address = models.CharField(max_length=200)
    gender = models.CharField(choices=sex, max_length=20)
    photo = models.ImageField(upload_to='pics/users', default=None)

    def __str__(self):
        return self.name

class Donation(models.Model):
    donor = models.ForeignKey(ExtendedUser, default=None, on_delete=models.CASCADE)
    food_type = models.CharField(max_length=100, default='Edible')
    quantity = models.CharField(max_length=100, default='1 kg')
    expiry_date = models.DateField(default='2025-10-10')

    def __str__(self):
        return f"Donation ID: {self.id} - {self.food_type} from {self.donor.username}"

