from django.shortcuts import render
from django.http import HttpResponse

def post_list(request):
    return render(request, 'blog/post_list.html', {})

def flor(request):
    return render(request, 'blog/flor.html', {})

def portao(request):
    return HttpResponse("Tú chengou a la puerta de tu casa")

def sala(request):
    return HttpResponse("llegaste a la sala, ¡sientate en el sofa!")

def cuarto(request):
    return HttpResponse("ahora estas en el cuarto :), ¡ahora puedes dormir!")

