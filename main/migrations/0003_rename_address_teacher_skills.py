# Generated by Django 5.0 on 2023-12-10 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_coursecategory_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='address',
            new_name='skills',
        ),
    ]