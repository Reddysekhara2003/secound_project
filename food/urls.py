from django.urls import path
from .views import *
app_name='food'
urlpatterns=[
    path('biriyani/',biriyani,name='biriyani'),
    path('parota/',parota,name='parota')
    
]