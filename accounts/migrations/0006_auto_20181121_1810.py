# Generated by Django 2.0.9 on 2018-11-21 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20181001_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='full_name',
            new_name='first_name',
        ),
    ]
