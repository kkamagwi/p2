# Generated by Django 3.1.7 on 2021-03-19 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_lesson_refreshment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessonsegment',
            old_name='skill',
            new_name='hardskill',
        ),
        migrations.AddField(
            model_name='lessonsegment',
            name='softskill',
            field=models.TextField(blank=True),
        ),
    ]
