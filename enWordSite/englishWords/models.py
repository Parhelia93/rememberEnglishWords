from django.db import models
from django.urls import reverse
# Create your models here.


class WordCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    progress_cat = models.ForeignKey('ProgressCat', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cat', kwargs={'catId':self.slug})

    class Meta:
        verbose_name = 'English_Words' # change model name in admin panel


class ProgressCat(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('progCat', kwargs={'progCat':self.pk})


class Word(models.Model):
    word = models.CharField(max_length=50)
    translation = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    example = models.TextField(blank=True)
    ime_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    word_cat = models.ForeignKey(WordCategory, on_delete=models.CASCADE, null=True, related_name='word_cat')

    def __str__(self):
        return self.word

    # def get_absolute_url(self):
    #     return reverse('progCat', kwargs={'progCat':self.pk})