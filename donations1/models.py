from django.db import models

# Create your models here.


class Donation1(models.Model):
    food_name = models.CharField(max_length=100, default='Edible')
    category = models.CharField(max_length=100)
    donation_date = models.DateField()

    def __str__(self):
        return f"{self.food_name}"