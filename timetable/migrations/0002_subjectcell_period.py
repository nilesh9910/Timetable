# Generated by Django 3.0.8 on 2020-08-02 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectcell',
            name='period',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]