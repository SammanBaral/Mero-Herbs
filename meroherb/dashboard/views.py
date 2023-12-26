from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.

def dashboardView(request):
    return render(request,'dashboard/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect ("core:login")

def sellerprofile(request):
    return render(request,'dashboard/profile.html')

def home(request):
    return render(request,'dashboard/dashboard.html')