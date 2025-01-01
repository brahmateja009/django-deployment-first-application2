from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def f1(request):
    return HttpResponse("<h2> Good morning User...!! Have a nice day..</h2><hr/>");
def f2(request):
    return HttpResponse("<h2> Good afternoon User...!! Hope you are doing good..</h2><hr/>");
def f3(request):
    return HttpResponse("<h2> Good Evening User...!! How was your day..</h2><hr/>");