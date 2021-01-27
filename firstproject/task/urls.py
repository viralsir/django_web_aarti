from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="task-home"),
    path("add",views.addtask,name="task-add")
]