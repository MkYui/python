# Generated by Django 2.0.9 on 2018-11-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_catalognews_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalognews',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
