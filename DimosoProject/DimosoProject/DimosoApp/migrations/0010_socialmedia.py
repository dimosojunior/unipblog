# Generated by Django 3.2.5 on 2022-02-09 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0009_alter_myuser_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_url', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=200, null=True)),
                ('whatsapp_url', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
