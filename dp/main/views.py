from django.shortcuts import render


def menu(request):
    context = {
        'name1': 'Restorant',
        'name2': 'Здравец',
    }
    return render(request, 'main/menu.html', context)
