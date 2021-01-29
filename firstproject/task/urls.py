from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="task-home"),
    path("new",views.addtask,name="task-add")
]