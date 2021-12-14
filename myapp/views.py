from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from django.db.models import Count
def index(req):
    return HttpResponse('hi')
def findCandidate(req,workTitle):
    
    #skills_of_job0 = Job.objects.all()[0].skills.all()
    candidates_with_title = Candidate.objects.filter(title=workTitle)
    skills_of_job0 = Job.objects.get(title = workTitle).skills.all()
    print(skills_of_job0)
    list_of_matching_candidates = candidates_with_title.filter(skills__in=skills_of_job0)
    print(list_of_matching_candidates)
    sorted_list = list_of_matching_candidates.annotate(count = Count('name')).order_by('-count')
    print(sorted_list)
    
    print('With count:')
    for candidate in sorted_list:
        print(candidate,candidate.count)
    test = querysetTostr(skills_of_job0)
    
    return HttpResponse(f'skills_of_job0 = {querysetTostr(skills_of_job0)}<br> list_of_matching_candidates = {querysetTostr(list_of_matching_candidates)} <br> sorted_list = {querysetTostr(sorted_list)}')

def querysetTostr(queryset):
    arr = []
    for query in queryset:
        arr.append(str(query))
    return arr
