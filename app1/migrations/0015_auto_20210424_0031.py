# Generated by Django 3.2 on 2021-04-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_auto_20210424_0022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Now',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='book_table',
            name='Date_coming',
        ),
    ]
