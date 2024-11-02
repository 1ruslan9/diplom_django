from django.shortcuts import render


def login(request):
    context = {
        'title': 'ERILIYA - Авторизация'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'ERILIYA - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'ERILIYA - Кабинет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...