# -*- coding: utf-8 -*-
from django.shortcuts import *
from django.http import *
from .models import *
from django.utils import dateparse, timezone


def index(req):
    return render(req, 'diseases/index.html', {'activate': {'index': 'active'}})


def disease(req):
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
            return redirect('/dis')
        else:
            dis.name = req.POST["name"]
            dis.description = req.POST["description"]
            dis.save()

    return render(req, 'diseases/diseaseById.html',
                  {'activate': {'none': 'active'}, 'disease': dis})


def case(req):
    cases = Case.objects.all()
    params = {}

    if 'location_id' in req.GET:
        params['location_id'] = req.GET["location_id"]
        if params['location_id'] != '-1': cases = cases.filter(location=params['location_id'])
        params['dateStart'] = dateparse.parse_date(req.GET["dateStart"])
        params['dateFinish'] = dateparse.parse_date(req.GET["dateFinish"])
        cases = cases.filter(dateStart__range=(params['dateStart'], params['dateFinish']))
    else:
        params['location_id'] = -1
        params['dateStart'] = timezone.datetime.min
        params['dateFinish'] = timezone.datetime.max

    return render(req, 'diseases/case.html',
                  {'activate': {'case': 'active'}, 'cases': cases, 'locations': Location.objects.all(),
                   'params': params})


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
            return redirect('/dis')
        else:
            case.name = Person.objects.get(pk=req.POST["person_id"])
            case.dateStart = dateparse.parse_date(req.POST["dateStart"])
            case.dateFinish = dateparse.parse_date(req.POST["dateFinish"])
            case.disease = Disease.objects.get(pk=req.POST["disease_id"])
            case.description = req.POST["description"]
            case.location = Location.objects.get(pk=req.POST["location"])
            case.save()

    return render(req, 'diseases/caseByID.html',
                  {'activate': {'none': 'active'}, 'case': case, 'diseases': Disease.objects.all(),
                   'locations': Location.objects.all(), 'persons': Person.objects.all()})
