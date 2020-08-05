# Generated by Django 3.0.8 on 2020-08-04 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timetable', '0003_auto_20200802_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='all_sub', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
