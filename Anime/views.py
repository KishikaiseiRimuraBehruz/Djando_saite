from django.shortcuts import render
from .models import Anime

# Create your views here.
def home(request):
    anime = Anime.objects.all()

    context = {'anime': anime}

    return render(request, 'Anime/home.html', context)

def about(request):
    return render(request, 'Anime/about.html')
