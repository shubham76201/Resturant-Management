# Generated by Django 3.1.7 on 2021-04-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0047_order_now_date1'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_table',
            name='booking_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
