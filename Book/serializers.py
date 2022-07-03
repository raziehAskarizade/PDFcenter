from rest_framework import serializers
from .models import InfoBook
from taggit.models import Tag
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)


class InfoBookSerializers(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = InfoBook
        fields = (
            'name', 'author', 'translator', 'photo', 'details', 'publish_date', 'page_num', 'rate', 'rate_number',
            'views',
            'pdf', 'id', 'slug', 'tags',)


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'slug',)
