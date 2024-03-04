from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import user_collection, User
from .serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt
from bson import ObjectId
from datetime import datetime


def index(request):
    return render(request, "index.html")


def books(request):
    data = [
        {"id": 1, "title": "The Book of Eli", "year": "2015"},
        {"id": 2, "title": "Avatar - The Last Air Bender", "year": "2024"},
        {"id": 3, "title": "Last Summer", "year": "2009"},
    ]
    HttpResponse.status_code = 200
    response = JsonResponse({"status": HttpResponse.status_code, "data": data})
    response["Content-Type"] = "application/json"
    return response


@csrf_exempt
def users(request):
    response = {}
    message = ""
    data = []
    if request.method == "GET":
        user = list(user_collection.find({}))

        for u in user:
            u["_id"] = str(u["_id"])
            u["createdAt"] = u["createdAt"] if "createdAt" in u else ""
            u["updatedAt"] = u["updatedAt"] if "updatedAt" in u else ""

        serializers = UserSerializer(user, many=True)
        data = serializers.data
        HttpResponse.status_code = 200
        message = "Get data success"
    elif request.method == "POST":
        user_data = JSONParser().parse(request)
        new_user = {
            "name": user_data["name"],
            "email": user_data["email"],
            "createdAt": datetime.now(),
            "updatedAt": datetime.now(),
        }
        serializers = UserSerializer(data=new_user)
        if serializers.is_valid():
            user_collection.insert_one(new_user)
            HttpResponse.status_code = 201
            message = "Data added successfully"
        else:
            HttpResponse.status_code = 500
            message = "Failed to add"
    elif request.method == "PUT":
        user_data = JSONParser().parse(request)
    elif request.method == "DELETE":
        # user_data = JSONParser().parse(request)
        # user_collection.delete_one({""})
        print("delete id", request.GET.get("id"))

    response = JsonResponse(
        {"status": HttpResponse.status_code, "message": message, "data": data}
    )
    response["Content-Type"] = "application/json"
    return response
