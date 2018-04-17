from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Якщо у вас залишились питання,'
                                                             ' то задавайте їх мені за телефоном', '(095) 567-44-65']})
