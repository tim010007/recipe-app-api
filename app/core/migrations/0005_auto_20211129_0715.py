# Generated by Django 2.2 on 2021-11-29 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='tags',
            new_name='tag',
        ),
    ]