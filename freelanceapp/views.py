from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from users.models import CustomUser
from .models import Client
import pytz


def home(request):
    return render(request, "freelanceapp/home.html")


@login_required(login_url='/users/login')
def freelancer_view(request):
    

    return render(request,"freelanceapp/freelancer.html")


@login_required(login_url='/users/login')
def client_view(request):
        current_user = request.user
        client_profile = Client.objects.get(client=current_user)
        if client_profile:
            return render(request,"freelanceapp/client.html")
        else:
            return redirect("client_profile")
        
@login_required(login_url='/users/login')
def client_profile(request):
    if request.method == 'POST':
        client_ = request.user
        client_id = client_.id
        company_name = request.POST.get('company_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        timezone = request.POST.get('timezone')
        postal_code = request.POST.get('postal_code')

        client = Client(client_id= client_id,company_name=company_name, phone_number=phone_number, address=address, timezone=timezone, postal_code=postal_code)
        client.save()
        return redirect("home")
        

    else:
        timezones = pytz.all_timezones
        return render(request,"freelanceapp/client_profile.html",{'timezones': timezones})
        
