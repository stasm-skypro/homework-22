"""
Контроллеры, определённые внутри приложения catalog.
"""

from django.shortcuts import render


def home_page(request):
    return render(request, "home.html")


def contacts_page(request):
    return render(request, "contacts.html")
