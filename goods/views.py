from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'home - Каталог',
        'goods': [
        {'image': 'deps/images/goods/c62c5c9cc7103845819728cc0b3c2753.jpg',
         'name': 'Лезвия профессиональные',
         'description': 'Лезвия профессиональныеЛезвия профессиональныеЛезвия профессиональные',
         'price': 150.00},

         {'image': 'deps/images/goods/photo_2024-10-25_03-58-41.jpg',
         'name': 'Спортивный костюм фиолетовый',
         'description': 'Спортивный костюм фиолетовыйСпортивный костюм фиолетовыйСпортивный костюм фиолетовый',
         'price': 93.00},

         {'image': 'deps/images/goods/photo_2024-10-25_03-58-58.jpg',
         'name': 'Спортивный костюм черный',
         'description': 'Спортивный костюм черныйСпортивный костюм черныйСпортивный костюм черный',
         'price': 670.00},

         {'image': 'deps/images/goods/photo_2024-10-25_03-59-29.jpg',
         'name': 'Кофта спортивная фиолетовая',
         'description': 'Кофта спортивная фиолетоваяКофта спортивная фиолетоваяКофта спортивная фиолетовая',
         'price': 365.00},

         {'image': 'deps/images/goods/photo_2024-10-25_03-59-34.jpg',
         'name': 'Лосины черные',
         'description': 'Лосины черныеЛосины черныеЛосины черные',
         'price': 430.00},

         {'image': 'deps/images/goods/photo_2024-10-25_03-59-50.jpg',
         'name': 'Перчатки синие',
         'description': 'Перчатки синиеПерчатки синиеПерчатки синие',
         'price': 610.00},

         {'image': 'deps/images/goods/photo_2024-10-25_03-59-53.jpg',
         'name': 'Перчатки черные',
         'description': 'Перчатки черныеПерчатки черныеПерчатки черные',
         'price': 55.00},

         {'image': 'deps/images/goods/photo_2024-10-25_03-59-56.jpg',
         'name': 'Перчатки серые',
         'description': 'Перчатки серыеПерчатки серыеПерчатки серые',
         'price': 190.00},

         {'image': 'deps/images/goods/photo_2024-10-25_04-00-00.jpg',
         'name': 'Кофта спортивная черная',
         'description': 'Кофта спортивная чернаяКофта спортивная чернаяКофта спортивная черная',
         'price': 30.00},

         {'image': 'deps/images/goods/photo_2024-10-25_04-00-09.jpg',
         'name': 'Ботинки ИДЕЯ ОВЕРТЮРЕ',
         'description': 'Ботинки ИДЕЯ ОВЕРТЮРЕБотинки ИДЕЯ ОВЕРТЮРЕБотинки ИДЕЯ ОВЕРТЮРЕ',
         'price': 10.00},

         {'image': 'deps/images/goods/photo_2024-10-25_04-00-20.jpg',
         'name': 'Ботинки РИСПОРТ СКЕЙТС',
         'description': 'Ботинки РИСПОРТ СКЕЙТСБотинки РИСПОРТ СКЕЙТСБотинки РИСПОРТ СКЕЙТС',
         'price': 15.00},

         {'image': 'deps/images/goods/photo_2024-10-25_04-00-26.jpg',
         'name': 'Ботинки ИДЕЯ ЧОРУС',
         'description': 'Ботинки ИДЕЯ ЧОРУСБотинки ИДЕЯ ЧОРУСБотинки ИДЕЯ ЧОРУС',
         'price': 25.00},
        ]
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
