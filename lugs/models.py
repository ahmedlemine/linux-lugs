from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Lug(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True, default='http://linuxlugs.com')
    cover_image = models.ImageField(default='lug_default_photo.png', upload_to='lug_cover_images')
    # TODO: make it a list
    country = models.CharField(max_length=100, null=False, blank=False)
    province = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=False, blank=False)
    # location on map (lat, long)
    # time
    contact_person = models.CharField(max_length=100, null=True, blank=True)
    # TODO: make it a list
    contact_info = models.TextField(null=True, blank=True)
    # youtube_channel = models.URLField(null=True, blank=True)
    donate_link = models.URLField(null=True, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('lug-detail', kwargs={'pk': self.pk})

    def save(self):
        super().save()

        img = Image.open(self.cover_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.cover_image.path)