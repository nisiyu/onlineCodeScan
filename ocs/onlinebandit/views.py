from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello,world!")

def userview(request, user_id):
    return HttpResponse(str(user_id))

def planview(request, user_id, plan_id):
    return HttpResponse(str(user_id)+' '+str(plan_id))