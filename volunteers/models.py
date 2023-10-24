from django.contrib.auth.models import User
from django.db import models

from stores.models import Store

# Create your models here.

locations = [('Farmgate', 'Farmgate'), ('Dhanmondi', 'Dhanmondi'), ('Mohammadpur', 'Mohammadpur'),
             ('Moghbazar', 'Moghbazar'), ('Badda', 'Badda'), ('Mirpur', 'Mirpur'), ('Shamoli', 'Shamoli'),
            ('Adabor', 'Adabor'), ('Green Road', 'Green Road'),
             ('Uttara', 'Uttara'), ('Azimpur', 'Azimpur'), ('Khilkhet', 'Khilkhet'), ('Banani', 'Banani'),
             ('Nilkhet', 'Nilkhet'), ('Bashabo', 'Bashabo'), ('Rampura', 'Rampura'), ('Mouchak', 'Mouchak'),
             ('Mugdha', 'Mugdha'), ('Wari', 'Wari'), ('Shahabagh', 'Shahabagh'),
             ]
sex = [('Male','Male'), ('Female', 'Female')]


class Volunteer(models.Model):
    user=models.OneToOneField(User,default=None,on_delete=models.CASCADE)
    store=models.ForeignKey(Store,default=None,on_delete=models.CASCADE)
    is_available=models.BooleanField(default=True)



