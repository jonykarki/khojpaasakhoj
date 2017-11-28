from django.shortcuts import render
from .models import *
from .scrape import Scraper

# Create your views here.
def home(request):
    return render(request, 'khoj/home.html')

def search(request):
    q = request.GET.get("q")
    lc = request.GET.get("lc")
    
    data = Scraper("restaurant", "thamel", 1)
    data.scrape()

    post = Post.objects.filter(baddress__icontains=lc)
    context = {
        'post': post
    }

    return render(request, 'khoj/search.html', context)