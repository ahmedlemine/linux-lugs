# Generated by Django 2.2.2 on 2019-11-07 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugs', '0004_auto_20191106_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='lug',
            name='facebook',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='lug',
            name='gettogether_page',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='lug',
            name='telegram',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='lug',
            name='twitter',
            field=models.URLField(blank=True, default='', null=True),
        ),
    ]
