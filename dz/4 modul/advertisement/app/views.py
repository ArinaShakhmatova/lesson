from django.shortcuts import render
from .models import Adverisement
from django.http import HttpResponse



def index(request):
    advertisements = Adverisement.objects.all()
    context = {"advertisement": advertisements}
    return render(request, "index.html", context)


def top_sellers(request):
    return render(request, "top-sellers.html")


def advertisement_post(request):
    return render(request, "advertisement-pos.html")


def register(request):
    return render(request, "register.html")


def login(request):
    return render(request, "login.html")


def profile(request):
    return render(request, "profile.html")


