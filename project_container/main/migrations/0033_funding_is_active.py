# Generated by Django 4.2.13 on 2025-03-27 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_remove_hiringposition_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='funding',
            name='is_active',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
