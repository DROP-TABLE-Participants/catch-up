# Generated by Django 5.0.3 on 2024-03-30 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapers', '0005_history_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='source',
            field=models.CharField(max_length=7),
        ),
    ]
