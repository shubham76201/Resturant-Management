# Generated by Django 3.1.7 on 2021-04-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0052_auto_20210427_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_now',
            name='distance_from_home',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]