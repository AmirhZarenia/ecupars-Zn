# Generated by Django 5.1.1 on 2024-11-22 20:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_diagnosticstep_created_at_diagnosticstep_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivity',
            name='action',
            field=models.CharField(choices=[('create', 'ایجاد'), ('update', 'ویرایش'), ('delete', 'حذف')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useractivity',
            name='model_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useractivity',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='useractivity',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
