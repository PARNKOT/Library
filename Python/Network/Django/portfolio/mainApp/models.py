from django.db import models


# Create your models here.
class Project(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    last_updated = models.DateTimeField("last update")

    def __str__(self):
        return f"|Project#{self.number};{self.name}; {self.last_updated}|"

    def __repr__(self):
        return self.__str__()

