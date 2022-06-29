from django.db import models
from .validators import validate_file_extension
from taggit.managers import TaggableManager
from django_jalali.db import models as jmodels


class BookManager(models.Manager):
    def get_queryset(self):
        return super(BookManager, self).get_queryset().filter(status='published')


class InfoBook(models.Model):
    name = models.CharField(max_length=200)
    id = models.BigAutoField(primary_key=True)
    slug = models.SlugField(auto_created='name', blank=False, allow_unicode=True)
    author = models.CharField(max_length=200)
    translator = models.CharField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='photos', default='default.jpg', blank=True)
    details = models.TextField()
    publish_date = jmodels.jDateField(default='1401-01-01')
    page_num = models.IntegerField()
    rate = models.FloatField(default=0)
    rate_number = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    pdf = models.FileField(validators=[validate_file_extension], upload_to='PDFs')
    tags = TaggableManager()
    STATUS_LIST = (('draft', 'ذخیره نشده'), ('published', 'منتشر شده'),)
    status = models.CharField(max_length=10, choices=STATUS_LIST, default='draft')
    published = BookManager()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
