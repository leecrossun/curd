# Generated by Django 3.0.5 on 2020-05-03 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='my_field',
            new_name='is_good',
        ),
    ]
