# Generated by Django 5.2 on 2025-04-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_varified',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='verication_secret',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
