from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):


    context = {
        'title': 'ERILIYA - Главная',
        'content': "Магазин фигурного катания ERILIYA",
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'ERILIYA - О НАС',
        'content': "О нас",
        'text_on_page': "О насО насО насО насО насО наО насО насО насО насО насО насО нас",
    }

    return render(request, 'main/about.html', context)
