# Generated by Django 2.2.12 on 2022-01-15 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerowaste', '0004_auto_20220113_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
