from django.urls import path
from . import views

app_name = "Ask"

urlpatterns =[
    path('index/', views.index, name="index"),
]