# Generated by Django 5.1.1 on 2024-10-24 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_diagnosticstep_questions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticstep',
            name='letter',
            field=models.CharField(editable=False, max_length=1),
        ),
    ]
