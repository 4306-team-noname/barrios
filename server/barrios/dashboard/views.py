from django.shortcuts import redirect, render
from random import randint


def index(request):
    if request.user.is_authenticated:
        return render(
            request,
            "pages/dashboard/index.html",
            {
                "usage_difference": get_usage(request),
                "last_optimization": get_optimizations(request),
            },
        )
    else:
        return redirect("/accounts/login")


def get_usage(request):
    return randint(-50, 50)


def get_optimizations(request):
    dummy_opts = {
        "launch_name": "SPX29",
        "launch_date": "12/23/2023",
        "payload": [
            {
                "name": "ACY Insert",
                "amount": 50,
                "unit": "ACY Insert",
            },
            {
                "name": "KTO",
                "amount": 3,
                "unit": "KTO",
            },
            {"name": "Pretreat Tanks", "amount": 1, "unit": "Pretreat Tanks"},
            {"name": "Filter Inserts", "amount": 2, "unit": "Filter Inserts"},
            {"name": "Urine Receptacle", "amount": 1, "unit": "Urine Receptacle"},
            {"name": "EDVs", "amount": 5, "unit": "EDVs"},
            {"name": "O2", "amount": 168, "unit": "lbs"},
            {"name": "N2", "amount": 126, "unit": "lbs"},
            {"name": "Water", "amount": 200, "unit": "Liters"},
        ],
    }

    return dummy_opts


def get_forecasts(request):
    pass
