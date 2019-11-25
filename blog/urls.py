from django.urls import path
from . import views

urlpatterns = [
    path('',views.myblogs, name='myblogs'),
]
