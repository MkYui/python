# Generated by Django 2.0.8 on 2018-10-30 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_remove_catalognews_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalognews',
            name='port',
            field=models.BooleanField(default=False),
        ),
    ]