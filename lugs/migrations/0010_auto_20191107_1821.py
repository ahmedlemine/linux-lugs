# Generated by Django 2.2.2 on 2019-11-07 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugs', '0009_auto_20191107_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lug',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=128),
        ),
    ]
