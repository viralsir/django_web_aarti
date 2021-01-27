from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1>Hello wel come to the world of DJango</h1>");

# def greetings(request,name):
#     return HttpResponse("<h1> Hello "+name+" </h1>")

def greetings(request,name):
    return render(request,"hello/greetings.html",{
        "user_name":name
    })