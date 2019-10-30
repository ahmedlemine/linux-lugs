# Generated by Django 2.2.2 on 2019-10-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lug',
            name='cover_image',
            field=models.ImageField(default='lug_default_photo.png', upload_to='lug_cover_images'),
        ),
        migrations.AddField(
            model_name='lug',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='lug',
            name='contact_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lug',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lug',
            name='donate_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lug',
            name='province',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lug',
            name='website',
            field=models.URLField(blank=True, default='http://linuxlugs.com', null=True),
        ),
    ]