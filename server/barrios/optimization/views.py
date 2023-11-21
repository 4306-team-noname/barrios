from django.shortcuts import redirect, render
from .Optimizer import Optimizer


def index(request):
    if request.user.is_authenticated:
        return render(request, "pages/optimization/index.html")
    else:
        return redirect("/accounts/login")


def create_optimization(request, consumable):
    # grab flight plan from db
    # get latest usage rates from db
    optimizer = Optimizer(consumable)

    result = optimizer.run_optimization()

    return render("blahblah.html", {"optimization": result})
