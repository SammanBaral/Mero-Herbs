from django.db.models import Avg
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .decorators import allowed_users
from .forms import NewItemForm, EditItemForm
from .models import Category, Item, review,ItemImage
from django.contrib.auth.models import User
from django.contrib.auth.models import User,Group
from sellerform.forms import UserProfilePhotoForm
from .models import ItemImageGallery, ItemImage



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
    item_image_gallery = ItemImageGallery.objects.filter(item=item).first()

  
    if request.method == 'POST':
        star_rating = request.POST.get('rating')
        item_review = request.POST.get('item_review')
        review.objects.create(user=request.user, item=item, rating=star_rating, review_desp=item_review)

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
    product=Item.objects.filter(category=category)
    return render(request,'item/browse.html',{'items':product,'category':category})


def sellerform(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        # Check if the user exists
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Handle case where user doesn't exist
            return render(request, 'sellerform/sellerform.html', {'error': 'User does not exist'})

        # Check if the user should be granted seller status
        if user_should_be_seller(user):
            # Get or create the 'seller' group
            seller_group, created = Group.objects.get_or_create(name='seller')
            # Add user to 'seller' group
            user.groups.add(seller_group)

            # Now, handle the profile picture upload
            form = UserProfilePhotoForm(request.POST,request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = user
                profile.save()
                return redirect('item:home')
            else:
                return render(request, 'sellerform/sellerform.html', {'error': 'Form is not valid'})
        else:
            return render(request, 'sellerform/sellerform.html', {'error': 'User does not meet requirements to be a seller'})

    else:
        form = UserProfilePhotoForm()

    return render(request, 'sellerform/sellerform.html', {'form': form})


def user_should_be_seller(user):
    # Example criteria:
    # Check if the user has been active for a certain period (e.g., 30 days)
    # active_threshold = timedelta(days=1)
    # if timezone.now() - user.date_joined < active_threshold:
    #     return False

    # # Check if the user has verified their email
    # if not user.email or not user.email_verified:
    #     return False

    # # Check if the user has completed a certain number of orders
    # min_orders_completed = 10
    # user_orders_completed = user.orders.filter(status='completed').count()
    # if user_orders_completed < min_orders_completed:
    #     return False

    # # Add more conditions here based on your application's requirements
    # # ...

    # If all criteria are met, return True
    return True