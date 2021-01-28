from django.db import models
from django.shortcuts import render, reverse

# Create your models here.

class File(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    image = models.ImageField()
    date = models.DateTimeField()


    class Meta:
        verbose_name = 'Fayl'
        verbose_name_plural = 'Fayllar'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})