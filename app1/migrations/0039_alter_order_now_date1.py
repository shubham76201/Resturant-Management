# Generated by Django 3.2 on 2021-04-24 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0038_rename_date_order_now_date1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_now',
            name='date1',
            field=models.DateField(max_length=200),
            preserve_default=False,
        ),
    ]
