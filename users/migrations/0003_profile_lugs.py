# Generated by Django 2.2.2 on 2019-11-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugs', '0003_auto_20191025_1754'),
        ('users', '0002_profile_real_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='lugs',
            field=models.ManyToManyField(to='lugs.Lug'),
        ),
    ]
