from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['user_name']
        email=request.POST['email']
        password=request.POST['password']
        phone=request.POST['phone']
        if User.objects.filter(username=user_name).exists():
            return HttpResponse('This Username has already taken. Please take different username.')
        else:
            new_user=User(first_name=first_name, last_name=last_name, username=user_name, email=email, password=password)
            new_user.save()
            new_profile=UserProfile(user=new_user,phone=phone)

            new_profile.save()
            return HttpResponse('Your Registration has successfully done.')
    return render(request,'registration.html')  


def user_login(request):
    if request.method=='POST':
        user_name=request.POST['user_name']
        password=request.POST['password']
        user=authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            #return HttpResponse('Your login has successfully done.')
            return redirect('/')
        else:
            return HttpResponse('Wrong username or password')
            #messages.error(request, 'User or password is incorrect')
    return render(request, 'login.html')
def user_logout(request):
    logout(request)
    return redirect('/')