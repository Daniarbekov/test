# Generated by Django 4.1.7 on 2023-03-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_menuitems_named_url_menuitems_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitems',
            name='named_url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]