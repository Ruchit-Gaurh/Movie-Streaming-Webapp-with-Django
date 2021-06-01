from django.core.checks.messages import Error
from django.shortcuts import get_object_or_404, render
from .models import main_poster, upload_serie, episodesss, epi, category1_name, category1, category2_name, category2, category3_name, category3, category4_name, category4, category5_name, category5, category6_name, category6, category7_name, category7, category8_name, category8, category9_name, category9, category10_name, category10
from django.views.generic import TemplateView

# Create your views here.
def main_page(request):
    banner_title = main_poster.objects.values('mobile_title')
    poster = upload_serie.objects.get(title__contains=banner_title)
    # cat1 = category1.objects.all().order_by('?')
    cat1 = upload_serie.objects.filter(genres__icontains='Romantic Comedy').order_by('?')[:10]
    # cat2 = category2.objects.all().order_by('?')
    cat2 = upload_serie.objects.filter(genres__icontains='Suspense').order_by('?')[:10]
    # cat3 = category3.objects.all().order_by('?')
    cat3 = upload_serie.objects.filter(year__icontains=2021).order_by('?')[:10]
    # cat4 = category4.objects.all().order_by('?')
    cat4 = upload_serie.objects.filter(genres__icontains='Idol Drama').order_by('?')[:10]
    # cat5 = category5.objects.all().order_by('?')
    cat5 = upload_serie.objects.filter(genres__icontains='Fantasy').order_by('?')[:10]
    cat6 = category6.objects.all().order_by('?')
    cat7 = category7.objects.all().order_by('?')
    cat8 = category8.objects.all().order_by('?')
    cat9 = category9.objects.all().order_by('?')
    cat10 = category10.objects.all().order_by('?')
    cat1_name = category1_name.objects.all()
    cat2_name = category2_name.objects.all()
    cat3_name = category3_name.objects.all()
    cat4_name = category4_name.objects.all()
    cat5_name = category5_name.objects.all()
    cat6_name = category6_name.objects.all()
    cat7_name = category7_name.objects.all()
    cat8_name = category8_name.objects.all()
    cat9_name = category9_name.objects.all()
    cat10_name = category10_name.objects.all()
    recent = upload_serie.objects.all().order_by('-id')[:10]
    context = {"poster":poster, 'cat1':cat1, 'cat2':cat2, 'cat3': cat3, 'cat4':cat4, 'cat5':cat5, 'cat6':cat6, 'cat7':cat7, 'cat8':cat8, 'cat9':cat9, 'cat10':cat10,'cat1_name':cat1_name, 'cat2_name':cat2_name, 'cat3_name': cat3_name, 'cat4_name':cat4_name, 'cat5_name':cat5_name, 'cat6_name':cat6_name, 'cat7_name':cat7_name, 'cat8_name':cat8_name, 'cat9_name':cat9_name, 'cat10_name':cat10_name, 'recent':recent}
    return render(request, "main.html", context)


def series_detail_view(request, title=None):
    serie_view = get_object_or_404(upload_serie, url=title)
    episodes = episodesss.objects.all()
    epis = epi.objects.all()
    context = {'serie_view':serie_view, 'episodes':episodes, 'epis': epis}
    return render(request, "series_detail_view.html", context)



def play_view(request , number=None, title=None):
    episode = get_object_or_404(episodesss, onlyepisodenumber=number, parent_url=title)
    return render(request, "player.html", {'episode':episode})

def sitemap_func(request):
    return render(request, "sitemap.xml", {"foo":"bar"}, content_type="application/xhtml+xml")


def search_result_page(request):
    query = request.GET['query']
    uploadTitle = upload_serie.objects.filter(title__icontains=query)
    ktitle = upload_serie.objects.filter(korean_title__icontains=query)
    uploadTDK = uploadTitle.union(ktitle)
    genre = upload_serie.objects.filter(genres__icontains=query)
    uploadTDKG = uploadTDK.union(genre)
    noepisodes = upload_serie.objects.filter(episodes__icontains=query)
    uploadTDKGE = uploadTDKG.union(noepisodes)
    
    params = {'result': uploadTDKGE, 'query':query}
    return render(request, "search.html", params)