from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero
from django.urls import reverse
# Create your views here.


def index(request):
    all_superheros = Superhero.objects.all()
    context = {
        'all_superheros': all_superheros
    }
    return render(request, 'Superheros/index.html', context)


def details(request, superhero_id):
    hero = Superhero.objects.get(id=superhero_id)
    context = {
        'hero': hero
    }
    return render(request, 'superheros/details.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catch_phrase = request.POST.get('catch_phrase')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catch_phrase=catch_phrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('Superheros:index'))
    else:
        return render(request, 'Superheros/create.html')


def edit(request, hero_id):
    if request.method == 'POST':
        hero_edit = Superhero.objects.get(id=hero_id)
        hero_edit.name = request.POST.get('name')
        hero_edit.alter_ego = request.POST.get('alter_ego')
        hero_edit.primary_ability = request.POST.get('primary_ability')
        hero_edit.secondary_ability = request.POST.get('secondary_ability')
        hero_edit.catch_phrase = request.POST.get('catch_phrase')
        hero_edit.save()
        return HttpResponseRedirect(reverse('Superheros:index'))
    else:
        return render(request, 'Superheros/edit.html')
