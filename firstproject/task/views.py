from django.shortcuts import render
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
tasks=['check email','recharge the mobile ','send money','pay elect bill']
# Create your views here.
def home(request):
    return render(request,"task/home.html",{
        "tasks":tasks
    })

class newtaskform(forms.Form):
    task=forms.CharField(max_length=25)
    priority=forms.IntegerField(max_value=10,min_value=1)
    task_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    admin_date = forms.DateField(widget=AdminDateWidget())


def addtask(request):
    form=newtaskform()
    return render(request,"task/addtask.html",{
        "form":form
    })