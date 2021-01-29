from django.shortcuts import render,redirect
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
    priority=forms.IntegerField(max_value=7,min_value=1)
    # task_date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    # admin_date = forms.DateField(widget=AdminDateWidget(attrs={'type':'date'}))


def addtask(request):
    if request.method == 'POST' :
        form=newtaskform(request.POST)
        if form.is_valid():
            tasks.append(form.cleaned_data["task"])
            return redirect('task-home')
        else :
            return render(request, "task/addtask.html", {
                "form": form
            })
    form=newtaskform()
    return render(request,"task/addtask.html",{
        "form":form
    })