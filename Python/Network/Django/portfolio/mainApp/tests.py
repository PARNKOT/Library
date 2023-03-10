import django.db.models
from django.test import TestCase
from django.utils import timezone
from .models import Project

# Create your tests here.


def create_project(number, name):
    return Project.objects.create(number=number, name=name, last_updated=timezone.now())


def create_n_projects(n: int):
    out = []
    for i in range(n):
        out.append(create_project(i+1, f"Name{i}"))

    return out


class ProjectModelTests(TestCase):
    def test_fields(self):
        create_n_projects(3)

        for project in Project.objects.all():
            self.assertGreater(project.number, 0)


class IndexViewTests(TestCase):
    def test_projects_list(self):
        create_n_projects(3)

        projects = Project.objects.all()

        response = self.client.get("/projects/")
        self.assertSetEqual(response.context['projects_list'], projects)
        #self.assertQuerysetEqual(response.context['projects_list'], projects)

