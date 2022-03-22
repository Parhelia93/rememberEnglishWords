from django.db import models
from django.urls import reverse
# Create your models here.


class WordCategory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    progress_cat = models.ForeignKey('ProgressCat', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cat', kwargs={'catId':self.pk})


class ProgressCat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('progCat', kwargs={'progCat':self.pk})
