# Generated by Django 3.2 on 2021-04-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_auto_20210424_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_table',
            name='guest_no',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book_table',
            name='table_no',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book_table',
            name='table_type',
            field=models.CharField(max_length=200),
        ),
    ]
