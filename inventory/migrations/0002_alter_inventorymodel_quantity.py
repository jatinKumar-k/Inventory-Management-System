# Generated by Django 4.0.5 on 2023-04-29 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorymodel',
            name='Quantity',
            field=models.CharField(max_length=1000),
        ),
    ]
