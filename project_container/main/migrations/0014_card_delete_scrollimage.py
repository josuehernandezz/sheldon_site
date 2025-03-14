# Generated by Django 4.2.13 on 2024-06-04 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_issue_publication_issue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='card_img/')),
                ('title', models.CharField(max_length=300)),
                ('detail', models.CharField(max_length=2000)),
                ('alt', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ScrollImage',
        ),
    ]
