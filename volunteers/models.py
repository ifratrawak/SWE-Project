from django.contrib.auth.models import User
from django.db import models



# Create your models here.

locations = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Mohammadpur', 'Mohammadpur'),
             ('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'), ('Mirpur', 'Mirpur'), ('Shamoli', 'Shamoli'),
            ('Adabor', 'Adabor'), ('Green Road', 'Green Road'),
             ('Uttara', 'Uttara'), ('Azimpur', 'Azimpur'), ('Khilkhet', 'Khilkhet'), ('Banani', 'Banani'),
             ('Nilkhet', 'Nilkhet'), ('Bashabo', 'Bashabo'), ('Rampura', 'Rampura'), ('Mouchak', 'Mouchak'),
             ('Mugdha', 'Mugdha'), ('Wari', 'Wari'), ('Shahabagh', 'Shahabagh'),
             ]
sex = [('Male','Male'), ('Female', 'Female')]
class WebUser(models.Model):
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    location = models.CharField(choices=locations, max_length=100)
    address = models.CharField(max_length=200)
    gender = models.CharField(choices=sex, max_length=20)
    photo = models.ImageField(upload_to='images/users', default=None)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    user = models.OneToOneField(WebUser, default=None, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

