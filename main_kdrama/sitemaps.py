from django.contrib import sitemaps
from django.urls import reverse
from .models import upload_serie, episodesss

class StaticViewSitemap(sitemaps.Sitemap):


    def items(self):
        return [
            'main:search',
        ]

    def location(self, item):
        return reverse(item)

class slugsitemap(sitemaps.Sitemap):
    def items(self):
        return upload_serie.objects.all()

class episodes(sitemaps.Sitemap):
    def items(self):
        return episodesss.objects.all()