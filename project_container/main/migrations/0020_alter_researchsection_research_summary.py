# Generated by Django 4.2.13 on 2024-07-03 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_researchsection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researchsection',
            name='research_summary',
            field=models.TextField(max_length=10000),
        ),
    ]
