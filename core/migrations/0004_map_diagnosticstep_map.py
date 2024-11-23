# Generated by Django 5.1.1 on 2024-10-29 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_diagnosticstep_letter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='maps/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.issuecategory')),
            ],
        ),
        migrations.AddField(
            model_name='diagnosticstep',
            name='map',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='diagnostic_steps', to='core.map'),
        ),
    ]
