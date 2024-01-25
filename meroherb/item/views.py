from django.db.models import Avg
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .decorators import allowed_users
from .forms import NewItemForm, EditItemForm
from .models import Category, Item, review,ItemImage
from .models import ItemImageGallery, ItemImage
from django.db import IntegrityError



from decimal import Decimal

def mainpage(request):
    categories = Category.objects.all()


    new_products = Item.objects.annotate(
        avg_rating=Avg('review__rating')
    ).order_by('-created_at')[:12]

    new_products_with_images = []
    for product in new_products:
        item_image_gallery = ItemImageGallery.objects.filter(item=product).first()
        product_data = {
            'product': product,
            'image_url': item_image_gallery.images.first().image.url if item_image_gallery and item_image_gallery.images.exists() else None,
        }
        new_products_with_images.append(product_data)

    best_selling = Item.objects.annotate(avg_rating=Avg('review__rating')).order_by('-avg_rating')[:4]
    best_selling_with_images = []
    for product in best_selling:
        item_image_gallery = ItemImageGallery.objects.filter(item=product).first()
        product_data = {
            'product': product,
            'image_url': item_image_gallery.images.first().image.url if item_image_gallery and item_image_gallery.images.exists() else None,
        }
        best_selling_with_images.append(product_data)

    latest_products = Item.objects.order_by('-created_at')[:4]
    latest_products_with_images = []
    for product in latest_products:
        item_image_gallery = ItemImageGallery.objects.filter(item=product).first()
        product_data = {
            'product': product,
            'image_url': item_image_gallery.images.first().image.url if item_image_gallery and item_image_gallery.images.exists() else None,
        }
        latest_products_with_images.append(product_data)


    deal_day = Item.objects.annotate(avg_rating=Avg('review__rating')).order_by('-avg_rating')[:2]
    deal_day_with_images = []
    for product in deal_day:
        item_image_gallery = ItemImageGallery.objects.filter(item=product).first()
        product_data = {
            'product': product,
            'image_url': item_image_gallery.images.first().image.url if item_image_gallery and item_image_gallery.images.exists() else None,
        }
        deal_day_with_images.append(product_data)


    top_rated = Item.objects.annotate(avg_rating=Avg('review__rating')).order_by('-avg_rating')[:4]
    top_rated_with_images = []
    for product in top_rated:
        item_image_gallery = ItemImageGallery.objects.filter(item=product).first()
        product_data = {
            'product': product,
            'image_url': item_image_gallery.images.first().image.url if item_image_gallery and item_image_gallery.images.exists() else None,
        }
        top_rated_with_images.append(product_data)


    trending_products = Item.objects.order_by('price')[:4]
    trending_products_with_images = []
    for product in trending_products:
        item_image_gallery = ItemImageGallery.objects.filter(item=product).first()
        product_data = {
            'product': product,
            'image_url': item_image_gallery.images.first().image.url if item_image_gallery and item_image_gallery.images.exists() else None,
        }
        trending_products_with_images.append(product_data)

    #calculating discount and adding the data to the item discount field in model 
    for product in new_products:
        if product.discount > 0:
            discounted_price = Decimal(product.price) * (1 - Decimal(product.discount) / 100)
            product.discounted_price = discounted_price
    
    return render(request, 'item/main.html', {
        
        'deals': deal_day,
        'categories': categories,
        'deal_day_with_images': deal_day_with_images,
        'trending_products_with_images':trending_products_with_images,
        'new_products_with_images':new_products_with_images,
        'best_selling_with_images': best_selling_with_images,
        'latest_product_with_images': latest_products_with_images,
        'top_rated_with_images':top_rated_with_images,


    })

 

def is_valid_queryparam(param):
    return param != '' and param is not None and param !=0.0   #for price

def browse(request): 
    query = request.GET.get('query', '')
    category_id= request.GET.get('category', 0)
    categories=Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    price_min=request.GET.get('input-min',0)
    price_max=request.GET.get('input-max',0)
    for product in items:
            if product.discount > 0:
                print("discount")
                discounted_price = Decimal(product.price) * (1 - Decimal(product.discount) / 100)
                product.discounted_price = discounted_price
                print(discounted_price)
    
    
    items_with_images = []
    for product in items:
        item_image_gallery = ItemImageGallery.objects.filter(item=product).first()
        product_data = {
            'product': product,
            'image_url': item_image_gallery.images.first().image.url if item_image_gallery and item_image_gallery.images.exists() else None,
        }
        items_with_images.append(product_data)
   
    
    if category_id:
        items=items.filter(category_id=category_id)

        for item in items:
            if(item.discount > 0):
                discounted_price = Decimal(product.price) * (1 - Decimal(product.discount) / 100)
                item.discounted_price=discounted_price
                print(discounted_price)

       
        items_with_images = []
       

        for product in items:
            item_image_gallery = ItemImageGallery.objects.filter(item=product).first()
            product_data = {
                'product': product,
                'image_url': item_image_gallery.images.first().image.url if item_image_gallery and item_image_gallery.images.exists() else None,
            }
            items_with_images.append(product_data)

    elif query:
        items = items.filter(name__icontains=query)
        items_with_images = []
        for product in items:
            item_image_gallery = ItemImageGallery.objects.filter(item=product).first()
            product_data = {
                'product': product,
                'image_url': item_image_gallery.images.first().image.url if item_image_gallery and item_image_gallery.images.exists() else None,
            }
            items_with_images.append(product_data)

    elif is_valid_queryparam(price_min) and is_valid_queryparam(price_max):
        items = Item.objects.filter(price__range=(float(price_min),float(price_max)))
        items_with_images = []
        for product in items:
            item_image_gallery = ItemImageGallery.objects.filter(item=product).first()
            product_data = {
                'product': product,
                'image_url': item_image_gallery.images.first().image.url if item_image_gallery and item_image_gallery.images.exists() else None,
            }
            items_with_images.append(product_data)

    return render(request,'item/browse.html',{
        'items_with_images': items_with_images,
        'query': query,
        'categories': categories,
        
    })

from django.shortcuts import redirect

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    reviews = review.objects.filter(item=item)
    item_image_gallery = ItemImageGallery.objects.filter(item=item).first()

    if request.method == 'POST':
        star_rating = request.POST.get('rating')
        item_review = request.POST.get('item_review')

        try:
            review.objects.create(user=request.user, item=item, rating=star_rating, review_desp=item_review)
        except IntegrityError:
            messages.error(request, "Please fill all the fields")
        else:
            # Redirect to the same detail page after successful review submission so that the user should not resubmit data on reload
            return redirect('item:detail', pk=pk)

    return render(request, 'item/detail.html', {
        'item': item,
        'reviews': reviews,
        'item_image_gallery': item_image_gallery,
    })


@login_required
@allowed_users(allowed_roles=['seller'])
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST)
        image_files = request.FILES.getlist("images")

        if form.is_valid():
            if len(image_files) > 4:
                messages.error(request, "You can upload a maximum of 4 images.")
                return render(request, 'item/form.html', {
                'form': form,
                'title': 'New item',}
                )
            
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            # Create an ItemImageGallery instance and associate it with the Item
            item_image_gallery = ItemImageGallery.objects.create(item=item)

            # Add each image to the ItemImageGallery
            for image_file in image_files:
                item_image = ItemImage.objects.create(item=item, image=image_file)
                item_image_gallery.images.add(item_image)

            messages.success(request, "New item created")
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
    products=Item.objects.filter(category=category)

    items_with_images = []
    for product in products:
        item_image_gallery = ItemImageGallery.objects.filter(item=product).first()
        product_data = {
            'product': product,
            'image_url': item_image_gallery.images.first().image.url if item_image_gallery and item_image_gallery.images.exists() else None,
        }
        items_with_images.append(product_data)

    return render(request,'item/browse.html',{'items_with_images':items_with_images,'category':category})