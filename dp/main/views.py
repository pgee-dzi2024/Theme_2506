from django.shortcuts import render
from .models import *


def menu(request):
    groups = Group.objects.all()
    menu = MenuItem.objects.all()

    context = {
        'groups': groups,
        'menu': menu,
    }
    return render(request, 'main/menu.html', context)
