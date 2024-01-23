from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile
from sellerform.models import SellerAccount  # Import your UserProfile model

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'first_name', 'last_name', 'contact_number']


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        pass

class BioLocationForm(forms.ModelForm):
    class Meta:
        model = SellerAccount
        fields = ['bio', 'location']