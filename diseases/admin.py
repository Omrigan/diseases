from django.contrib import admin
from .models import *

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'dateCreation')
    list_filter = ['dateCreation']
    search_fields = ['name']
class CaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'dateStart', 'dateFinish', 'disease', 'description')
    list_filter = ['dateStart', 'dateFinish', 'disease']
    search_fields = ['name']

admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Case, CaseAdmin)
