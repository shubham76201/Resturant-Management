# Generated by Django 3.1.7 on 2021-04-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_auto_20210424_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_table',
            name='date',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]