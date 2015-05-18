from django.db import models


class Disease(models.Model):
    name = models.CharField(max_length=1000)
    dateCreation = models.DateTimeField('date published')
    description = models.CharField(max_length=4000)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Case(models.Model):
    name = models.CharField(max_length=300)
    dateStart = models.DateTimeField('Start case')
    dateFinish = models.DateTimeField('Finish case', blank=True, null=True)
    disease = models.ForeignKey(Disease)
    description = models.CharField(max_length=4000)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name


