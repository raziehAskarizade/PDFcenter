# Generated by Django 4.0.5 on 2022-06-29 04:27

import Book.validators
from django.db import migrations, models
import django.db.models.manager
import django_jalali.db.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoBook',
            fields=[
                ('slug', models.SlugField(allow_unicode=True, auto_created='name')),
                ('name', models.CharField(max_length=200)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=200)),
                ('translator', models.CharField(blank=True, max_length=200)),
                ('photo', models.ImageField(blank=True, default='default.jpg', upload_to='photos')),
                ('details', models.TextField()),
                ('publish_date', django_jalali.db.models.jDateField(default='1401-01-01')),
                ('page_num', models.IntegerField()),
                ('rate', models.FloatField(default=0)),
                ('rate_number', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('pdf', models.FileField(upload_to='PDFs', validators=[Book.validators.validate_file_extension])),
                ('status', models.CharField(choices=[('draft', 'ذخیره نشده'), ('published', 'منتشر شده')], default='draft', max_length=10)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('name',),
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]