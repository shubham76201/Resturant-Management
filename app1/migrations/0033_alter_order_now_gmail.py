# Generated by Django 3.2 on 2021-04-24 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0032_alter_order_now_date_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_now',
            name='gmail',
            field=models.EmailField(max_length=220),
            preserve_default=False,
        ),
    ]