# Generated by Django 4.2.13 on 2024-06-04 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_publication_publication_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='Issue',
            new_name='issue',
        ),
    ]
