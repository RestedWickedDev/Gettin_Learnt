from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def guitar(request):
    return render(request, 'guitar.html')

def art(request):
    return render(request, 'art.html')

def game(request):
    return render(request, 'game.html')
