# Generated by Django 5.0.6 on 2024-06-06 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_api', '0003_alter_order_total_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]