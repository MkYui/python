# Generated by Django 2.0.8 on 2018-09-25 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_users_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileusers',
            name='users',
        ),
        migrations.DeleteModel(
            name='ProfileUsers',
        ),
    ]
