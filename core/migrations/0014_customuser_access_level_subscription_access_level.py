# Generated by Django 5.1.1 on 2024-11-21 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_issuecategory_logo_alter_mapcategory_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='access_level',
            field=models.IntegerField(choices=[(1, 'کاربر سطح 1'), (2, 'کاربر سطح 2'), (3, 'کاربر سطح 3'), (4, 'کاربر سطح 4')], default=1),
        ),
        migrations.AddField(
            model_name='subscription',
            name='access_level',
            field=models.IntegerField(choices=[(1, 'کاربر سطح 1'), (2, 'کاربر سطح 2'), (3, 'کاربر سطح 3'), (4, 'کاربر سطح 4')], default=1),
        ),
    ]
