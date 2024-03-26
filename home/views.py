from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    persons = [
        {'name': "Messi", 'team':'Argentina','jersey':'10'},
        {'name': "Nadim", 'team':'Barcelona','jersey':'8'},
        {'name': "Rijvi", 'team':'Manchester City','jersey':'30'},
        {'name': "Shakib", 'team':'Bangladesh','jersey':'72'},
        {'name': "Afridi", 'team':'Pakistan','jersey':'10'}
        
    ]
    for person in persons:
        print(person)

    return render(request, 'index.html',context = {'persons': persons})