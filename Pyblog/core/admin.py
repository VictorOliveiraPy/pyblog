from django.contrib import admin
from Pyblog.core.models import Publish

# Register your models here.
from django.utils.html import format_html


class PublishModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo_img']

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}" />', obj.photo)

    photo_img.short_description = 'foto'


admin.site.register(Publish, PublishModelAdmin)
