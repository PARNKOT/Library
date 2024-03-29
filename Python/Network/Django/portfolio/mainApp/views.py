from django.shortcuts import render, get_object_or_404
import django.http as http
from django.template import loader
from .models import Project

# Create your views here.

biography = """
Hello! My name is Egor<br/>
My nickname is Parnkot<br>
I am programmer<br>
Welcome to my portfolio!<br>
"""


def index(request):
    #return render(request, "mainApp/index3.html")
    return render(request, "mainApp/title.html", context={"biography": biography})


def index_json(request):
    return http.JsonResponse({"name": "Parnkot", "Age": 25})


def projects(request):
    projects_list = Project.objects.all()
    template = loader.get_template("mainApp/index.html")
    context = {
        "projects_list": projects_list,
    }
    return http.HttpResponse(template.render(context, request))


def detail(request: http.HttpRequest, project_id):
    if request.method == "GET":
        return http.HttpResponse(get_object_or_404(Project, id=project_id))
        # try:
        #     return http.HttpResponse(Project.objects.get(id=project_id))
        # except Exception:
        #     raise http.Http404(Exception(f"There is no project with id {project_id}"))
    else:
        return http.HttpResponseNotFound()


def new_project(request):
    if request.method == "GET":
        return render(request, "mainApp/project.html", {})

