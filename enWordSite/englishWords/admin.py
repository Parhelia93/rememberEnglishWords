from django.contrib import admin
from englishWords.models import *
# Register your models here.


class WordCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}


class ProgressCatAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}


class WordAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("word",)}


admin.site.register(WordCategory,WordCategoryAdmin)
admin.site.register(ProgressCat,ProgressCatAdmin)
admin.site.register(Word,WordAdmin)