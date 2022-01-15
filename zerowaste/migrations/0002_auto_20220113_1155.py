# Generated by Django 2.2.12 on 2022-01-13 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zerowaste', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Ward',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.MumbaiWardBoundary2Jan2022', to_field='ward_id'),
        ),
        migrations.AlterField(
            model_name='user',
            name='prabhag',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.MumbaiPrabhagBoundaries3Jan2022V2', to_field='prabhag_no'),
        ),
    ]
