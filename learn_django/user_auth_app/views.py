from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Image


def home(request):
    return render (request,'home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        print(username,password)
        user = User.objects.filter(username=username)
        if user:
            messages.error(request,"mail id already in use :(")
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username,password=password)
            messages.info(request,"account {} created successfully :)".format(username))
    return render(request,'signup.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email,password=password)
        if user is not None:
            messages.success(request,"login successfull :)")
            login(request,user)
            print("logged in")
            return redirect('index')
        else:
            messages.error(request,"invalid credentials :(")
            return redirect('login')

    return render(request,'login.html')

def onlyloggedin(request):
    if request.user.is_authenticated:
        print(request.user.username)
        print("yes")
        return render(request,'onlyloggedin.html')
    else:
        messages.error(request,"please login to continue :(")
        return redirect('login')

def index(request):
    if request.user.is_authenticated:
        data = Image.objects.filter(user=request.user.id)
        context = {
            'data':data,
            'username':request.user.username[:-10]
        }
        return render(request,"display.html",context)
    else:
        return redirect('login')
    
def logout_user(request):
    logout(request)
    return redirect('login')


