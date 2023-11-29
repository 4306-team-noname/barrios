from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import AnalysisForm


def index(request):
    if request.user.is_authenticated:
        return redirect("/dashboard")
    else:
        return render(request, "index.html")


def get_form(request):
    if request.method == "POST":
        form = AnalysisForm(request.POST)
        if form.is_valid():
            analysis_type = form.cleaned_data["analysis_type"]
            if analysis_type == "Optimization":
                return render(request, "components/optimizationform.html")
            elif analysis_type == "Usage":
                return render(request, "components/usageform.html")
            elif analysis_type == "Forecast":
                return render(request, "components/forecastform.html")
        else:
            form = AnalysisForm()
