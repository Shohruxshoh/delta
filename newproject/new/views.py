from django.shortcuts import render
from .models import File
from django.db.models import Q
# Create your views here.

def index(request):
    # fayls = File.objects.all()[:3]
    fayls = File.objects.all().order_by('-date')[:3]
    return render (request, 'new/index.html', {'fayls': fayls})


def search_result(request):
    query = request.GET.get('search')
    search_obj = File.objects.filter(
        Q(title__icontains=query)| Q(text__icontains=query)
    )
    return render (request, 'new/search.html', {'search_obj': search_obj, 'query': query})

def post_detail(request, slug):
    fayls = File.objects.get(slug__iexact = slug)
    return render(request, 'new/post_detail.html', {'post': fayls})