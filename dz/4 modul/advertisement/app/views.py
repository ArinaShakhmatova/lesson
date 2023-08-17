from django.shortcuts import render
from .models import Adverisement
from .forms import AdvertisementForm
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect



def index(request):
    advertisements = Adverisement.objects.all()
    context = {"advertisement": advertisements}
    return render(request, "index.html", context)


def top_sellers(request):
    return render(request, "top-sellers.html")


def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Adverisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse("main-page")
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form': form}
    return render(request, "advertisement-post.html", context)


def register(request):
    return render(request, "register.html")


def login(request):
    return render(request, "login.html")


def profile(request):
    return render(request, "profile.html")


