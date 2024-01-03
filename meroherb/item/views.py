from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .forms import NewItemForm, EditItemForm
from .models import Category, Item

def is_valid_queryparam(param):
    return param != '' and param is not None and param !=0.0

def browse(request): 
    query = request.GET.get('query', '')
    category_id= request.GET.get('category', 0)
    categories=Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    print(items)
    price_min=request.GET.get('input_min',0)
    price_max=request.GET.get('input_max',0)

    if category_id:
        items=Item.objects.filter(category_id=category_id)
        print(items)

    elif query:
        items = Item.objects.filter(name__icontains=query)
        print(query)

   
    elif is_valid_queryparam(price_min) and is_valid_queryparam(price_max):
        items = Item.objects.filter(price__range=(float(price_min),float(price_max)))

    return render(request,'item/browse.html',{
        'items': items,
        'query': query,
        'categories': categories,
        'price_max':price_max,
        'price_min':price_min,

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

