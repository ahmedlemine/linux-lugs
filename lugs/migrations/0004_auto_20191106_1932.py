# Generated by Django 2.2.2 on 2019-11-06 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugs', '0003_auto_20191025_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='lug',
            name='youtube_channel',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='lug',
            name='contact_person',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]