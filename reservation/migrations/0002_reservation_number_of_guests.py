# Generated by Django 5.0.6 on 2024-09-03 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='number_of_guests',
            field=models.IntegerField(default=0),
        ),
    ]