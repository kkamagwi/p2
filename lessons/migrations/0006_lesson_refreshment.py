# Generated by Django 3.1.7 on 2021-03-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_auto_20210319_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='refreshment',
            field=models.TextField(default='ferreshment is here'),
        ),
    ]
