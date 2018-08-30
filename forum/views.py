from django.shortcuts import render, get_object_or_404
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

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)

    # board = Board.objects.get(pk=pk)
    return render(request, 'forum/topics.html', {'board': board})


