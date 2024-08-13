# Generated by Django 4.2.13 on 2024-07-03 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_labmember_position_alter_labmember_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('research_summary', models.CharField(max_length=5000)),
                ('image', models.ImageField(upload_to='research_section_img/')),
            ],
        ),
    ]
