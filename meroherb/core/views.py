from django.shortcuts import redirect, render
from .forms import SignupForm, LoginForm
from item.models import Category, Item
from django.contrib import messages
from item.decorators import unauthenticated_user
from userprofile.models import UserProfile 

@unauthenticated_user
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create User instance
            user = form.save()

            # Create UserProfile instance
            user_profile = UserProfile.objects.create(
                user=user,
                username=form.cleaned_data['username'],
                contact_number=form.cleaned_data['contact_number'],
                location=form.cleaned_data['location'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
            )

            # Set the default profile picture for the user
            user_profile.photo = 'default_user.png'
            user_profile.save()

            messages.success(request, "Registered successfully!")
            return redirect('/login')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {'form': form})
