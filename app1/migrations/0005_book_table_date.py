# Generated by Django 3.2 on 2021-04-23 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_book_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_table',
            name='date',
            field=models.CharField(max_length=255),
            
        ),
    ]