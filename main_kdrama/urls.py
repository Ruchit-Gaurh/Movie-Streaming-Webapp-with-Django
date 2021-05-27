from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .views import main_page, series_detail_view, play_view, search_result_page, sitemap_func

urlpatterns = [
    path('', main_page),
    path("series/<slug:title>", series_detail_view, name="series_detail_view"),
    path("series/<slug:title>/episode<int:number>", play_view),
    path("search/results", search_result_page),
    path("sitemap.xml", sitemap_func)
]