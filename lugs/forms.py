from django.forms import ModelForm
from .models import Lug, Post
from cities_light.models import City


class LugForm(ModelForm):
    class Meta:
        model = Lug
        fields = [
        'name',
        'city',
        'meetup_place',
        'description',
        'cover_image',
        'website',
        'contact_person',
        'contact_info',
        'donate_link',
        'youtube_channel',
        'twitter',
        'facebook',
        'telegram'
        ]


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
        'title',
        'text'
        ]


class FindLugByCityForm(ModelForm):
    class Meta:
        model = Lug
        fields = [
        'city',
        ]