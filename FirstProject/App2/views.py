from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def f22(request):
    time=datetime.datetime.now();
    msg="<h2>Hello User..!!<br/><br/> server date & time::"+str(time)+"</h2><hr/>"
    return HttpResponse(msg);