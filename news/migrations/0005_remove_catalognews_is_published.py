# Generated by Django 2.0.8 on 2018-09-27 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_catalognews_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalognews',
            name='is_published',
        ),
    ]