from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Este é meu primeiro site utilizando django")

