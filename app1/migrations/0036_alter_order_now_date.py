# Generated by Django 3.2 on 2021-04-24 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0035_order_now_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_now',
            name='date',
            field=models.DateField(max_length=255),
            preserve_default=False,
            
        ),
    ]
