# Generated by Django 3.2.4 on 2021-06-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='cast',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='open_time',
            field=models.TimeField(),
        ),
    ]
