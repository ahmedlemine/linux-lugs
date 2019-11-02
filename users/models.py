from django.db import models
from django.contrib.auth.models import User
from lugs.models import Lug
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    real_name = models.CharField(max_length=100, null=True, blank=True, default="")
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    lugs = models.ManyToManyField(Lug)

    def __str__(self):
        return self.user.username
    
    #fix for profile not created issue
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)