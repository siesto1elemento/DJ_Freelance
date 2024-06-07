from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "freelanceapp/home.html")


@login_required(login_url='/users/login')
def freelancer_view(request):
    return render(request,"freelanceapp/freelancer.html")