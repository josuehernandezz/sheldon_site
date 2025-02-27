# Generated by Django 4.2.13 on 2024-06-03 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_publication_publication_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='issue',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='pages',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='volume',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='year',
            field=models.PositiveBigIntegerField(null=True),
        ),
    ]
