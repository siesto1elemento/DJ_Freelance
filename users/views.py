from django.shortcuts import render,HttpResponse,redirect
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

@csrf_exempt
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        
        role = request.POST.get('role')
        is_client = (role == 'client')
        is_freelancer = (role == 'freelancer')
        

        if password1 != password2:
            return render(request,"users/registration.html")

            
            

        new_profile = CustomUser(
            first_name=first_name,
            last_name=last_name,
            email=email,
            country=country,
            is_client=is_client,
            is_freelancer=is_freelancer,
            
        )
        new_profile.set_password(password1)
        new_profile.save()

        user = authenticate(username=email,password=password1)
        if user is not None:
            login(request, user)



        return render(request,"users/login.html")

    else:
        return render(request,"users/registration.html")
    

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)


        return HttpResponse("you are authenticated")
    
    else:
        return render(request, "users/login.html")
    

@csrf_exempt
def user_logout(request):
    logout(request)
    return redirect('register')
