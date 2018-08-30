from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Board


# def home(request):
#     boards = Board.objects.all()
#     context = {
#         'boards': boards,
#     }
#     return render(request, 'forum/home.html', context)

def home(request):
    boards = Board.objects.all()
    return render(request, 'forum/home.html', {'boards': boards})
