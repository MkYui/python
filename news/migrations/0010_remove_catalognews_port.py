# Generated by Django 2.0.8 on 2018-10-30 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_catalognews_port'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalognews',
            name='port',
        ),
    ]
