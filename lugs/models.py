from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.contrib.auth.models import User
from linux_lugs.utils import unique_slug_generator
from django.urls import reverse
from PIL import Image
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from cities_light.models import City


class Lug(models.Model):
    name = models.CharField(verbose_name='LUG Name', max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=128, null=False, blank=False, default='')
    description = models.TextField(verbose_name='Description', help_text='About LUG, activities, focus, agenda, timing, etc.', null=True, blank=True)
    website = models.URLField(verbose_name='LUG Website', null=True, blank=True, default='')
    cover_image = ProcessedImageField(verbose_name='LUG Cover Image/Logo', default='lug_default_photo.png', upload_to='lug_cover_images',
                                           processors=[ResizeToFill(338, 200)],
                                           format='JPEG',
                                           options={'quality': 60})
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    meetup_place = models.CharField(verbose_name='Meetup Place', help_text='Place where LUG members meet (restaurant, coffee shop, etc.)', max_length=250, null=True, blank=True)
    contact_person = models.CharField(verbose_name='Contact Person', max_length=100, null=True, blank=True)
    contact_info = models.CharField(verbose_name='Contact Info', help_text='How to contact LUG organizers (250 characters max).', max_length=250, null=True, blank=True)
    donate_link = models.URLField(verbose_name='Donation Page URL', help_text='Link to page where this LUG accepts donations.', default='', null=True, blank=True)
    youtube_channel = models.URLField(default='', null=True, blank=True)
    twitter = models.URLField(default='', null=True, blank=True)
    facebook = models.URLField(default='', null=True, blank=True)
    telegram = models.URLField(default='', null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('lug-detail', kwargs={'slug': self.slug})


# a pre-save signal to generate a slug and save it
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Lug)