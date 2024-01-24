# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserProfileForm
from django.contrib import messages
from userprofile.models import UserProfile
@login_required
def userprofile(request):
    user = request.user

    try:
        user_profile_instance = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile_instance = None

    user_profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=user_profile_instance)
    password_change_form = PasswordChangeForm(user)

    print("Request method:", request.method)

    if request.method == 'POST':
        if 'user-details-form-submit' in request.POST:
            user_profile_form = UserProfileForm(request.POST, instance=user_profile_instance)
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
        return redirect('userprofile:userprofile')
    else:
        form = UserProfileForm(instance=user_profile_instance)
        password_change_form = PasswordChangeForm(request.user)

    print("Rendering userprofile.html")
    return render(request, 'userprofile/userprofile.html', {'user': user, 'user_profile_form': user_profile_form, 'password_change_form': password_change_form})

# @login_required
# @user_passes_test(lambda user: user.groups.filter(name='seller').exists())
# def update_bio_location(request):
#     user = request.user

#     try:
#         seller_profile = SellerAccount.objects.get(user=user)
#     except SellerAccount.DoesNotExist:
#         messages.error(request, 'Seller profile does not exist. Please complete the seller registration first.')
#         return redirect('userprofile:userprofile')

#     if request.method == 'POST':
#         form = BioLocationForm(request.POST, initial={'bio': seller_profile.bio, 'location': seller_profile.location})

#         if form.is_valid():
#             bio = form.cleaned_data['bio']
#             location = form.cleaned_data['location']

#             # Update SellerProfile
#             seller_profile.bio = bio
#             seller_profile.location = location
#             seller_profile.save()

#             messages.success(request, 'Bio and location updated successfully.')
#             print("Form is valid. Data saved successfully.")
#         else:
#             messages.error(request, 'Invalid form data. Please check your input.')
#             print("Form is invalid. Errors:", form.errors)

#         # return redirect('userprofile:userprofile')
#     else:
#         form = BioLocationForm(initial={'bio': seller_profile.bio, 'location': seller_profile.location})

#     return render(request, 'userprofile/userprofile.html', {'form': form})
