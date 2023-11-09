from django.shortcuts import render


def index(request):
    return render(request, "pages/supply/index.html")
