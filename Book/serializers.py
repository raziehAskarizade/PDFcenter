from rest_framework import serializers
from .models import InfoBook
from taggit.models import Tag


class InfoBookSerializers(serializers.ModelSerializer):
    class Meta:
        model = InfoBook
        fields = (
            'name', 'author', 'translator', 'photo', 'details', 'publish_date', 'page_num', 'rate', 'rate_number',
            'views',
            'pdf',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
