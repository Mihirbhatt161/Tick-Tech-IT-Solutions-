from django.shortcuts import render,redirect
from home.models import contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    return render(request, 'index.html',)

def about(request):

    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method=="POST":
        name= request.POST.get("name")
        email= request.POST.get("email")
        desc= request.POST.get("desc")
        contact=contact(name="name",email="email",desc="desc")
        contact.save()
        
    
    return render(request, 'contact.html')
    



def loginUser(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request,"login.html")
    return render(request, "login.html")

def logoutuser(request):
    logout(request)
    return redirect("/login")