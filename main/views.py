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
        'title': 'ERILIYA - Про НАС',
        'content': "Про нас",
        'text_on_page': "Здесь будет представлена основная описательная информация о нашем интернет-магазине",
    }

    return render(request, 'main/about.html', context)
