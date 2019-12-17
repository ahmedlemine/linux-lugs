from rest_framework import serializers
from .models import Lug
from cities_light.models import City

class LugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lug
        fields = ['pk', 'name', 'slug', 'city', 'added_by', 'date_added', 'meetup_place']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'display_name']