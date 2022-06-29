from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe
from .models import InfoBook
from taggit.models import Tag
from django.db.models import Count
from rest_framework.decorators import api_view
from .serializers import InfoBookSerializers, TagSerializer
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET'])
def book_list(self, tag_slug=None):
    object_list = InfoBook.published.all()
    tags_list = InfoBook.tags.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    serialize_obj = InfoBookSerializers(object_list, many=True)
    serialize_tags = TagSerializer(tags_list, many=True)

    context = {'books': serialize_obj.data, 'tags_list': serialize_tags.data, 'tag': tag}
    return Response(mark_safe(context), status=status.HTTP_200_OK)


@api_view(['GET'])
def book_detail(request, objectId, slug):
    book = get_object_or_404(InfoBook, id=objectId, slug=slug, status='published')
    book_tag_id = book.tags.values_list('id', flat=True)
    related_book = InfoBook.published.filter(tags__in=book_tag_id).distinct().exclude(id=book.id).annotate(
        tags_num=Count('tags')).order_by('-tags_num')[:5]

    serialize_book = InfoBookSerializers(book)
    serialize_related_book = InfoBookSerializers(related_book, many=True)

    context = {'book': serialize_book.data, 'related_book': serialize_related_book.data}

    return Response(mark_safe(context), status=status.HTTP_200_OK)
