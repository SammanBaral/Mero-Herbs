from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout
# Create your views here.

def dashboardView(request):

    return render(request,'dashboard/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect ("dashboard:login")