from django.forms import ModelForm
from .models import Lug


class LugForm(ModelForm):
    class Meta:
        model = Lug
        fields = [
        'name',
        'city',
        'description',
        'cover_image',
        'website',
        'contact_person',
        'contact_info',
        'donate_link'
        ]