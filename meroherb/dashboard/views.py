from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User,Group
from item.models import Item
from .models import Comment
from .forms import CommentForm


# Create your views here.

    

def dashboardView(request):
    items=Item.objects.all()

    return render(request,'dashboard/dashboard.html',{'items':items})

def logout_view(request):
    logout(request)
    return redirect ("core:login")

def sellerprofile(request, pk):
    seller_info = get_object_or_404(User, pk=pk)
    comments = Comment.objects.filter(seller=seller_info)
    comment_form = CommentForm()

    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.seller=seller_info
                comment.save()
                return redirect('dashboard:dashboard')

    return render(request, 'dashboard/Profile.html', {
        'seller_info': seller_info,
        'comment_form': comment_form,
        'comments':comments
    })
    


def home(request):
    # items=Item.objects.all()
    # return render(request,'dashboard/dashboard.html')
    return dashboardView(request)



