# Generated by Django 2.2.2 on 2019-11-15 16:15

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lugs', '0016_auto_20191115_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lug',
            name='cover_image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='lug_cover_images'),
        ),
    ]