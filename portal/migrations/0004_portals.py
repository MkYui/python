# Generated by Django 2.0.8 on 2018-10-29 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.CatalogPortal')),
            ],
        ),
    ]
