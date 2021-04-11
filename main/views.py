from django.shortcuts import render
from main.models import Character
from django.http import HttpResponse


def main_page(request):
    characters = request.GET.get('filter')
    characters_query = Character.objects.all()
    return render(request, 'list.html', {"characters": characters_query})
