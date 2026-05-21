from django.contrib import admin
from django.utils.text import slugify
from django.contrib import admin
# Document modelini buradaki listeye eklediğinden emin ol:
from .models import GeneralSetting, ImageSetting, Skill, SocialMedia, Document
from core.models import *


@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

    class Meta:
        model = GeneralSetting


@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'file', 'updated_date', 'created_date']
    search_fields = ['name', 'description', 'file']
    list_editable = ['description', 'file']

    class Meta:
        model = ImageSetting


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'name', 'description', 'updated_date', 'created_date']
    list_editable = ['order', 'name', 'description']
    # Eğer search_fields vs. içinde de 'percentage' varsa onu da 'description' yap.
    class Meta:
        model = Skill


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'link', 'icon', 'updated_date', 'created_date']
    search_fields = ['link', 'icon']
    list_editable = ['order', 'link', 'icon']

    class Meta:
        model = SocialMedia


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id','order','slug','file', 'button_text', 'updated_date', 'created_date']
    search_fields = ['slug', 'button_text']
    list_editable = ['order', 'slug', 'button_text', 'file']

    class Meta:
        model = Document
