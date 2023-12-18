from django.shortcuts import redirect, render
# from items.models import Categories,Items
from .forms import SignupForm, LoginForm
from item.models import Category, Item
# Create your views here.
# information about website like type of request get post

def browse(request):
    items=Item.objects.filter(is_sold=False )[0:6]  #not showing sold items and limiting the items to 6 while displaying them
    categories=Category.objects.all()


    #passing request so that the request will be available in the template
    return render(request,'item/browse.html',{
        'categories': categories,
        'items':items,
    })


# def contact(request):
#     return render(request, 'core/contact.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form=SignupForm()


    return render(request,'core/signup.html',{
        'form':form
    })





