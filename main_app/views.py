from django.shortcuts import render
from .models import Comics
from django.views.generic import CreateView

def home(request):
    return render(request, 'home.html')

def exclusive(request):
    return render(request, 'exclusive.html')

def comics_index(request):
    comics = Comics.objects.all()  # Retrieve all comics
    return render(request, 'comics/detail.html', {
        'comics': comics
    })

def comic_detail(request, comic_id):
    comic = Comics.objects.get(id=comic_id)
    return render(request, 'comics/detail.html', {
        'comic': comic
    })

def hire_me(request):
    return render(request, 'hire_me.html')

class ComicsCreate(CreateView):
    model = Comics
    fields = ['title', 'price', 'stock', 'written_by', 'characters']
