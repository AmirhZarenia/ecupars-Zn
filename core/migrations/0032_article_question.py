# Generated by Django 5.1.1 on 2025-02-08 15:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_option_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.question'),
        ),
    ]
