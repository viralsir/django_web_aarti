from django.urls import path
from . import views
urlpatterns=[
    path("index/",views.home,name="hello-home"),
    path("greetings/<str:name>",views.greetings,name="hello-greetings")
]