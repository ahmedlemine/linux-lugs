# Generated by Django 2.2.2 on 2019-11-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_lugs'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube_channel',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
