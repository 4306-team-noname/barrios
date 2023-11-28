from django.http import HttpResponse
from django.shortcuts import redirect, render
from random import randint


def index(request):
    if request.user.is_authenticated:
        usage_difference = randint(-50, 50)
        return render(
            request,
            "pages/usage/index.html",
            {"usage_difference": usage_difference, "current_page": "usage"},
        )
    else:
        return redirect("/accounts/login")
