from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "hello.html")


def books(request):
    return HttpResponse("Books")
