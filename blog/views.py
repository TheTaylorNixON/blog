from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def posts_list(request):
    n = ['Artem', 'Vika', 'Alex', 'Zed']
    return render(request, 'blog/index.html', context={'names': n} )