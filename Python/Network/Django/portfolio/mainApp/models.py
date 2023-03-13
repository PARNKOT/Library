from django.db import models


# Create your models here.


class Project(models.Model):
    access_choices = (("Public", "Public"), ("Private","Private"))

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    access = models.CharField(max_length=20, choices=access_choices)
    created = models.DateTimeField("last update")
    image = models.ImageField(null=True)

    def __str__(self):
        return f"Project {self.name}. Created on: {self.created}. Access: {self.access}"

    def __repr__(self):
        return self.__str__()

    class Meta:
        db_table = "Project"
