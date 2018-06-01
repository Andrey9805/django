from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Мои контакты: ', 'Телефон: +7(917)679-39-43','Почта: grigorev.man@gmail.com']}) 
