from django.contrib import admin
from englishWords.models import *
# Register your models here.


class WordCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}


class ProgressCatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}


class ProgressCatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}


admin.site.register(WordCategory,WordCategoryAdmin)
admin.site.register(ProgressCat,ProgressCatAdmin)