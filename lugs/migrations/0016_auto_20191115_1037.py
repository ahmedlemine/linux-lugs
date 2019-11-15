# Generated by Django 2.2.2 on 2019-11-15 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lugs', '0015_auto_20191112_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lug',
            name='contact_info',
            field=models.TextField(blank=True, null=True, verbose_name='Contact Info'),
        ),
        migrations.AlterField(
            model_name='lug',
            name='contact_person',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Contact Person'),
        ),
        migrations.AlterField(
            model_name='lug',
            name='cover_image',
            field=models.ImageField(default='lug_default_photo.png', upload_to='lug_cover_images', verbose_name='LUG Cover Image'),
        ),
        migrations.AlterField(
            model_name='lug',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='lug',
            name='donate_link',
            field=models.URLField(blank=True, default='', null=True, verbose_name='Donation Page URL'),
        ),
        migrations.AlterField(
            model_name='lug',
            name='gettogether_page',
            field=models.URLField(blank=True, default='', null=True, verbose_name='GetTogether Page'),
        ),
        migrations.AlterField(
            model_name='lug',
            name='name',
            field=models.CharField(max_length=100, verbose_name='LUG Name'),
        ),
        migrations.AlterField(
            model_name='lug',
            name='website',
            field=models.URLField(blank=True, default='http://linuxlugs.com', null=True, verbose_name='LUG Website'),
        ),
    ]