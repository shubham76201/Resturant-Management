# Generated by Django 3.1.7 on 2021-04-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_book_table_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_table',
            name='guest_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book_table',
            name='table_no',
            field=models.IntegerField(),
        ),
    ]