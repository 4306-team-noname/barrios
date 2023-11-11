from django.http import HttpResponse
from django.shortcuts import redirect, render


def index(request):
    if request.user.is_authenticated:
        return render(request, "pages/usage/index.html")
    else:
        return redirect("/accounts/login")
