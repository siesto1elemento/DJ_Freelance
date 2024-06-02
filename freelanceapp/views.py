from django.shortcuts import render

def home(request):
    return render(request, "freelanceapp/home.html")
