from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import error, success
from django.shortcuts import redirect, render
from .forms import LoginForm
from common.conditionalredirect import conditionalredirect


def sign_in(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, "pages/accounts/login.html", {"form": form})

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(f"username: {username}, password={password}")

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                success(request, f"Welcome back, {user.username}")
                return redirect("/dashboard")

        # form not valid | user not authenticated
        error(request, "Invalid username or password")
        return render(request, "pages/accounts/login.html", {"form": form})


def sign_out(request):
    logout(request)
    success(request, "You have been logged out")
    return conditionalredirect(request, "/accounts/login/")


def profile(request):
    if request.user.is_authenticated:
        return render(
            request,
            "pages/accounts/profile.html",
            context={"request": request, "current_page": "profile"},
        )
    else:
        return conditionalredirect(request, "/accounts/login/")
