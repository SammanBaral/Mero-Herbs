from venv import logger
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .forms import NewItemForm, EditItemForm
from .models import Category, Item, review
from django.contrib.auth.models import User

def browse(request): 
    query = request.GET.get('query', '')
    category_id= request.GET.get('category', 0)
    categories=Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    
    if category_id:
        items=items.filter(category_id=category_id)

    if query:
        items = items.filter(name__icontains=query)

    return render(request,'item/browse.html',{
        'items': items,
        'query': query,
        'categories': categories,
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    reviews = review.objects.filter(item=item)
  
    if request.method == 'POST':
        star_rating = request.POST.get('rating')
        item_review = request.POST.get('item_review')
        review.objects.create(user=request.user, item=item, rating=star_rating, review_desp=item_review)

    return render(request, 'item/detail.html', {
        'item': item,
        'reviews': reviews
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk= pk, created_by=request.user)
    item.delete()

    return redirect('item:browse')

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk= pk, created_by=request.user)


    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

def Category_view(request,pro):
    category=Category.objects.get(name=pro)
    product=Item.objects.filter(category=category)
    return render(request,'item/browse.html',{'items':product,'category':category})

# Create your views here.

