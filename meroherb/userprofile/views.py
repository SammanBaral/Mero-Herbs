from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserProfileForm
from django.contrib import messages
from userprofile.models import UserProfile
from django.core.exceptions import ValidationError

@login_required
def userprofile(request):
    user = request.user

    try:
        user_profile_instance = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile_instance = None

    user_profile_form = UserProfileForm(request.POST or None, request.FILES or None, instance=user_profile_instance)
    password_change_form = PasswordChangeForm(user)

    if request.method == 'POST':
        if 'user-details-form-submit' in request.POST:
            user_profile_form = UserProfileForm(request.POST, instance=user)
            try:
                if user_profile_form.is_valid():
                    user_profile_form.save()
                    messages.success(request, 'User details updated successfully.')
            except ValidationError as e:
                messages.error(request, f'Error updating user details: {e}')
            except Exception as e:
                messages.error(request, f'An unexpected error occurred: {e}')

        elif 'password-change-form-submit' in request.POST:
            try:
                password_change_form = PasswordChangeForm(user, request.POST)
                if password_change_form.is_valid():
                    password_change_form.save()
                    messages.success(request, 'Password changed successfully.')
            except ValidationError as e:
                messages.error(request, f'Error changing password: {e}')
            except Exception as e:
                messages.error(request, f'An unexpected error occurred: {e}')

        return redirect('userprofile:userprofile')
    else:
        user_profile_form = UserProfileForm(instance=user_profile_instance)
        password_change_form = PasswordChangeForm(request.user)

    return render(request, 'userprofile/userprofile.html', {'user': user, 'user_profile_form': user_profile_form, 'password_change_form': password_change_form})
