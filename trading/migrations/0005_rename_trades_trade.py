# Generated by Django 3.2.13 on 2022-05-21 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trading', '0004_auto_20220521_1304'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trades',
            new_name='Trade',
        ),
    ]
