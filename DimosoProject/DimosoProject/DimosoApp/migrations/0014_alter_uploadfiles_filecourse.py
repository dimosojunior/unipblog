# Generated by Django 3.2.5 on 2022-02-11 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0013_auto_20220210_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='filecourse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DimosoApp.filecourse'),
        ),
    ]
