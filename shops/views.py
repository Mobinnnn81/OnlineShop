from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    all_products = Product.objects.all()
    return render(request, "index.html", {"products": all_products})


def about(request):
    return render(request, "about.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("با موفقیت وارد شدید"))
            return redirect("Home")
        else:
            messages.success(request, ("مشکلی در لاگین بوجود اومد دوباره امتحان کنید"))
            return redirect("login")
    else:
        return render(request, "loginout.html")


def logout_user(request):
    logout(request)
    messages.success(request, ("خروج موفقیت آمیز"))
    return redirect("Home")
