# Generated by Django 2.2.2 on 2019-11-22 16:55

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lugs', '0020_remove_lug_gettogether_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lug',
            name='contact_info',
            field=models.CharField(blank=True, help_text='How to contact LUG organizers (250 characters max).', max_length=250, null=True, verbose_name='Contact Info'),
        ),
        migrations.AlterField(
            model_name='lug',
            name='cover_image',
            field=imagekit.models.fields.ProcessedImageField(default='lug_default_photo.png', upload_to='lug_cover_images', verbose_name='LUG Cover Image/Logo'),
        ),
        migrations.AlterField(
            model_name='lug',
            name='description',
            field=models.TextField(blank=True, help_text='About LUG, activities, focus, agenda, timing, etc.', null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='lug',
            name='donate_link',
            field=models.URLField(blank=True, default='', help_text='Link to page where this LUG accepts donations.', null=True, verbose_name='Donation Page URL'),
        ),
        migrations.AlterField(
            model_name='lug',
            name='meetup_place',
            field=models.CharField(blank=True, help_text='Place where LUG members meet (restaurant, coffee shop, etc.)', max_length=250, null=True, verbose_name='Meetup Place'),
        ),
    ]
