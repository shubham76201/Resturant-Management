# Generated by Django 3.2 on 2021-04-23 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_auto_20210424_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_table',
            name='date',
        ),
    ]
