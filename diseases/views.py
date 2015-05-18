# -*- coding: utf-8 -*-
from django.shortcuts import *
from django.http import *
from .models import *
from django.utils import dateparse, timezone


def index(req):
    return render(req, 'diseases/index.html', {'activate': {'index': 'active'}})


def disease(req):
    print(Disease.objects.all())
    return render(req, 'diseases/disease.html', {'activate': {'dis': 'active'}, 'diseases': Disease.objects.all()})


def diseaseById(req, dis_id):
    if dis_id == '0':  # Create
        if req.POST:
            dis = Disease(dateCreation=timezone.now())
        else:
            dis = {'id': 0, 'name': 'Новое заболевание'}
    else:
        dis = Disease.objects.get(pk=dis_id)

    if req.POST:
        if "delete" in req.POST:
            dis.delete()
        else:
            dis.name = req.POST["name"]
            dis.description = req.POST["description"]
            dis.save()

    return render(req, 'diseases/diseaseById.html',
                  {'activate': {'none': 'active'}, 'disease': dis})


def case(req):
    LOCATION = (
        ('1', 'Восточно-Сибирская'),
        ('2', 'Горьковская'),
        ('3', 'Дальневосточная'),
        ('4', 'Забайкальская'),
        ('5', 'Западно-Сибирская'),
        ('6', 'Калининградская'),
        ('7', 'Красноярская'),
        ('8', 'Куйбышевская'),
        ('9', 'Московская'),
        ('10', 'Октябрьская'),
        ('11', 'Приволжская'),
        ('12', 'Свердловская'),
        ('13', 'Северная'),
        ('14', 'Северо-Кавказская'),
        ('15', 'Юго-Восточная'),
        ('16', 'Южно-Уральская')
    )
    # for l in LOCATION:
    #     Location.objects.create(name=l[1])
    return render(req, 'diseases/case.html', {'activate': {'case': 'active'}, 'cases': Case.objects.all()})


def caseById(req, case_id):
    if case_id == '0':  # Create
        if req.POST:
            case = Case()
        else:
            case = {'id': 0, 'name': 'Новый случай заболевания'}
    else:
        case = Case.objects.get(pk=case_id)
    if req.POST:
        if "delete" in req.POST:
            case.delete()
        else:
            case.name = req.POST["name"]
            case.dateStart = dateparse.parse_date(req.POST["dateStart"])
            case.dateFinish = dateparse.parse_date(req.POST["dateFinish"])
            case.disease = Disease.objects.get(pk=req.POST["disease_id"])
            case.description = req.POST["description"]
            case.location = Location.objects.get(pk=req.POST["location"])
            case.save()
    return render(req, 'diseases/caseByID.html',
                  {'activate': {'none': 'active'}, 'case': case, 'diseases': Disease.objects.all(),
                   'locations': Location.objects.all()})
