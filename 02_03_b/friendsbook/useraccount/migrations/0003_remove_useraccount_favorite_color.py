# Generated by Django 3.2.6 on 2021-10-21 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_useraccount_favorite_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='favorite_color',
        ),
    ]