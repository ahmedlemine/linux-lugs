# Generated by Django 2.2.2 on 2019-11-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20191123_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='youtube_channel',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
