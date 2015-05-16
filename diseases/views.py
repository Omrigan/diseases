from django.shortcuts import *
from django.http import *
from .models import *
from django.utils import dateparse

def index(req):
    return render(req, 'diseases/index.html', {'activate': {'index': 'active'}})


def disease(req):
    print(Disease.objects.all())
    return render(req, 'diseases/disease.html', {'activate': {'dis': 'active'}, 'diseases': Disease.objects.all()})


def diseaseById(req, dis_id):

    # if dis_id == 0:
    #     dis = Disease.objects.create()
    #     return redirect("/div/" + dis.id)
    dis = Disease.objects.get(pk=dis_id)
    if req.POST:
        dis.name = req.POST["name"]
        dis.description = req.POST["description"]
        dis.save()
    return render(req, 'diseases/diseaseById.html',
                  {'activate': {'none': 'active'}, 'disease': dis })


def case(req):
    return render(req, 'diseases/case.html', {'activate': {'case': 'active'}, 'cases': Case.objects.all()})


def caseById(req, case_id):
    case = Case.objects.get(pk=case_id)
    if req.POST:
        case.name = req.POST["name"]
        case.dateStart = dateparse.parse_date(req.POST["dateStart"])
        case.dateFinish = dateparse.parse_date(req.POST["dateFinish"])
        case.disease.id = req.POST["disease_id"]
        case.description = req.POST["description"]
        case.save()
    return render(req, 'diseases/caseByID.html', {'activate': {'none': 'active'}, 'case': case, 'diseases': Disease.objects.all()})
