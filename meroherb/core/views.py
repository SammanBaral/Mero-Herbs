from django.shortcuts import redirect, render
# from items.models import Categories,Items
from .forms import SignupForm, LoginForm
from item.models import Category, Item
from django.contrib import messages
from item.decorators import unauthenticated_user


# Create your views here.
# information about website like type of request get post





@unauthenticated_user
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered successfully!")
            return redirect('/login')
    else:
        form=SignupForm()


    return render(request,'core/signup.html',{
        'form':form
    })





