# Generated by Django 3.1.7 on 2021-04-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='date',
        ),
        migrations.AddField(
            model_name='signup',
            name='password',
            field=models.CharField(default=0, max_length=122),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='signup',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
