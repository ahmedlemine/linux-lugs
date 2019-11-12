

from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.contrib.auth.models import User
from linux_lugs.utils import unique_slug_generator
from django.urls import reverse
from PIL import Image
from cities_light.models import City


class Lug(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(max_length=128, null=False, blank=False, default='')
    description = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True, default='http://linuxlugs.com')
    cover_image = models.ImageField(default='lug_default_photo.png', upload_to='lug_cover_images')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # country = models.CharField(max_length=100, null=False, blank=False)
    # province = models.CharField(max_length=100, null=True, blank=True)
    # city = models.CharField(max_length=100, null=False, blank=False)
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    contact_info = models.TextField(null=True, blank=True)
    donate_link = models.URLField(null=True, blank=True)
    gettogether_page = models.URLField(default="", null=True, blank=True)
    youtube_channel = models.URLField(default="", null=True, blank=True)
    twitter = models.URLField(default="", null=True, blank=True)
    facebook = models.URLField(default="", null=True, blank=True)
    telegram = models.URLField(default="", null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('lug-detail', kwargs={'slug': self.slug})

    def save(self):
        super().save()

        img = Image.open(self.cover_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.cover_image.path)

# a pre-save signal to generate a slug and save it
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Lug)