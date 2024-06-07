from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('freelancer_view',views.freelancer_view, name='freelancer_view'),
    

]