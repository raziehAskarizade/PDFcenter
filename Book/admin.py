from django.contrib import admin
from .models import InfoBook
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin


@admin.register(InfoBook)
class TopicAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('name', 'author', 'translator', 'status', 'tags', 'id')
    list_filter = ('status', 'name', 'tags', 'author',)
    search_fields = ('name', 'details',)
    ordering = ('status',)
    prepopulated_fields = {"slug": ("name",)}

    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%y/%m/%d _ %H:%M:%S')

    get_created_jalali.short_description = 'تاریخ ایجاد'
    get_created_jalali.admin_order_field = 'created'
