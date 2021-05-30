from re import template
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .views import main_page, series_detail_view, play_view, search_result_page, sitemap_func
from .sitemaps import StaticViewSitemap, slugsitemap, episodes
from django.views.generic.base import TemplateView


sitemaps={
    'sitemap': StaticViewSitemap,
    'snippet': slugsitemap,
    'episodes': episodes
}

app_name = 'main'

urlpatterns = [
    path('', main_page, name='main'),
    path("series/<slug:title>", series_detail_view, name="series_detail_view"),
    path("series/<slug:title>/episode<int:number>", play_view, name='seriewithepisode'),
    path("search/results", search_result_page, name='search'),
    path('sitemap_index.xml', sitemap,{'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", TemplateView.as_view(template_name="main/robots.txt", content_type="text/plain"))
]