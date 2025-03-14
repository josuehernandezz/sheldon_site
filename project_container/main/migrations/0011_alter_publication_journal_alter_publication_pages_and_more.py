# Generated by Django 4.2.13 on 2024-06-04 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_scrollimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='journal',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='pages',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='url',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='volume',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='year',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
    ]
