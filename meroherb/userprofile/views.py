
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserProfileForm
from .models import UserProfile
from django.contrib import messages

@login_required
def userprofile(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=request.user)

    user_profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=user_profile)
    password_change_form = PasswordChangeForm(user)

    print("Request method:", request.method)

    if request.method == 'POST':
        if 'user-details-form-submit' in request.POST:
            user_profile_form = UserProfileForm(request.POST, instance=user)
            if user_profile_form.is_valid():
                user_profile_form.save()
                messages.success(request, 'User details updated successfully.')

        elif 'password-change-form-submit' in request.POST:
            print("Processing password change form")
            # Process password change form
            password_change_form = PasswordChangeForm(user, request.POST)
            if password_change_form.is_valid():
                password_change_form.save()
                print("Password change form is valid. Redirecting...")
        return redirect('userprofile:editprofile')
    else:
        form = UserProfileForm(instance=user)
        password_change_form = PasswordChangeForm(request.user)

    print("Rendering userprofile.html")
    return render(request, 'userprofile/userprofile.html', {'user': user, 'user_profile_form': user_profile_form, 'password_change_form': password_change_form})
