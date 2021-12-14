from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from myapp.models import *
from django.db.models import Count

def index(req):
    workList = Job.objects.all() 
    print(workList)
    context = {"workList": workList}
    return render(req, "index.html", context)

