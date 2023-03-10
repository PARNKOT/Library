from django.urls import path
from . import views


app_name = "mainApp"

urlpatterns = [
    path("", views.index),
    path("json", views.index_json),
    path("projects/", views.projects, name="projects"),
    path("projects/new", views.new_project, name="new_project"),
    path("projects/<int:project_id>", views.detail),
]
