# Generated by Django 4.2.13 on 2024-10-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_labmember_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(max_length=2000),
        ),
    ]
