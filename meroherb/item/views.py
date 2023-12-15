from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .forms import NewItemForm
from .models import Item
def browse(request):
    item= get_list_or_404(Item)
    return render(request,'item/browse.html',{
        'items':item
    })

def detail(request, pk):
    item = get_object_or_404(Item,pk=pk)

    return render(request, 'item/detail.html',{
        'item':item
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

# Create your views here.
