from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index" ),
    path("fazza", views.fazza,name="fazza"),
    path("teena",views.teena,name="teena"),
    path("<str:name>", views.greet, name="greet"),
    
    
]