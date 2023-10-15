# Generated by Django 4.2.6 on 2023-10-14 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_remove_donation_user_donation_donor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='donations.extendeduser'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='food_type',
            field=models.CharField(default='sm', max_length=100),
        ),
    ]
