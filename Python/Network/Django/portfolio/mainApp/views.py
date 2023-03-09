from django.shortcuts import render
import django.http as http


# Create your views here.
def index(request):
    return http.HttpResponse("Hello!<br>My nickname is Parnkot<br>Welcome to my portfolio!")


def index_json(request):
    return http.JsonResponse({"name": "Parnkot", "Age": 25})