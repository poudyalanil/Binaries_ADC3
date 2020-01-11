from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)
        user.save()
        return redirect('/')
    else:
        return render(request,'user/register.html',context={})


def user_login(request):
    context={}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('profile'))
    else:
        context['error'] = "Provide valid credentials !!"
        return render(request, 'user/login.html',context)


def user_logout(request):
    if request.method=="POST":
        logout(request)
        return HttpResponseRedirect(reverse('login'))

def profile(request):
    context = {}
    context['user'] = request.user
    return render(request,'user/profile.html',context={})

