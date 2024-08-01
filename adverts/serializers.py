from rest_framework import serializers

from adverts.models import Advert


class AdvertSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source='category.name')
    city_name = serializers.CharField(source='city.name')

    class Meta:
        model = Advert
        fields = ['id', 'title', 'description', 'views', 'created', 'category', 'city', 'category_name', 'city_name', ]
        read_only_fields = ['views', 'category_name', 'city_name', ]
