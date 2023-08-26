from django.shortcuts import render
from .models import Adverisement
from .forms import AdvertisementForm
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect


def index(request):
    advertisements = Adverisement.objects.all()
    context = {"advertisement": advertisements}
    return render(request, "app/index.html", context)


def top_sellers(request):
    return render(request, "app/top-sellers.html")


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
    return render(request, "app/advertisement-post.html", context)


def register(request):
    return render(request, "app_auth/register.html")


def login(request):
    return render(request, "app_auth/login.html")


def profile(request):
    return render(request, "app_auth/profile.html")


