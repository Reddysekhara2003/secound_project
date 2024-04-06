from django.urls import path
from .views import *
app_name='drinks'
urlpatterns=[
    path('mh/',mh,name='mh'),
    path('natusara/',natusara,name='natusara')
    
]