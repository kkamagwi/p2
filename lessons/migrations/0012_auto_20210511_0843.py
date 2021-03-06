# Generated by Django 3.1.7 on 2021-05-11 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0011_auto_20210505_0536'),
    ]

    operations = [
        migrations.CreateModel(
            name='lsTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=127)),
                ('details', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='lessonsegment',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ls_set', to='lessons.lesson'),
        ),
        migrations.AddField(
            model_name='lessonsegment',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tag_set', to='lessons.lstag'),
        ),
    ]
