# Generated by Django 2.1.5 on 2019-01-19 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_auto_20190117_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='type_one',
            new_name='primary_type',
        ),
        migrations.RenameField(
            model_name='pokemon',
            old_name='type_two',
            new_name='secondary_type',
        ),
    ]
