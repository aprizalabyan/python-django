from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse


def index(request):
    return render(request, "hello.html")


def books(request):
    data = [
        { "id": 1, "title": "The Book of Eli", "year": "2015"},
        { "id": 2, "title": "Avatar - The Last Air Bender", "year": "2024"},
        { "id": 3, "title": "Last Summer", "year": "2009"},
    ]
    response = JsonResponse({"status": HttpResponse.status_code, "data": data})
    response['Content-Type'] = 'application/json'
    response['Access-Control-Allow-Origin'] = '*'
    return response
