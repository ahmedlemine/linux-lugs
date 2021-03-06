from django.db import models
from django.contrib.auth.models import User
from lugs.models import Lug
from PIL import Image
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from cities_light.models import City

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    real_name = models.CharField(max_length=100, null=True, blank=True, default="")
    image = ProcessedImageField(verbose_name='Profile Photo', default='default.jpeg', upload_to='profile_pics', blank=True,
                                           processors=[ResizeToFill(128, 128)],
                                           format='JPEG',
                                           options={'quality': 80})
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    lugs = models.ManyToManyField(Lug)
    twitter = models.URLField(default='', null=True, blank=True)
    facebook = models.URLField(default='', null=True, blank=True)
    youtube_channel = models.URLField(default='', null=True, blank=True)


    def __str__(self):
        return self.user.username
    
    # #fix for profile not created issue
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)