from django import forms
from .models import Item


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name','scientific_name', 'description', 'usage_and_benefits', 'price', 'quantity_available', 'image', )

        widgets = {
            'category': forms.Select(attrs={
                'class': 'category_input'
                
            }),

            'name': forms.TextInput(attrs={
                'class': 'name_input',  # Apply the text-input class from your CSS
                'placeholder':'Name'
            }),

            'scientific_name': forms.TextInput(attrs={
                'class': 'name_input',  # Apply the text-input class from your CSS
                'placeholder':'Scientific name'

            }),

            'description': forms.Textarea(attrs={
                'class': 'description_input',  # Apply the text-input-description class from your CSS
                'placeholder':'Description'

            }),

            'usage_and_benefits': forms.Textarea(attrs={
                'class': 'usage_input',  # Apply the text-input-usage-benefit class from your CSS
                'placeholder':'Usage and benefits'

            }),

            'price': forms.TextInput(attrs={
                'class': 'price_input',  # Apply the text-input-price-field class from your CSS
                'placeholder':'Price'

            }),

            'quantity_available': forms.TextInput(attrs={
                'class': 'quantity_input'  # Apply the text-input-quantity-field class from your CSS
            }),

            'image': forms.FileInput(attrs={
                'class': 'image_input'
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','scientific_name', 'description', 'usage_and_benefits', 'price', 'quantity_available', 'image', )

        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'name_input',  # Apply the text-input class from your CSS
                'placeholder':'Name'
            }),

            'scientific_name': forms.TextInput(attrs={
                'class': 'name_input',  # Apply the text-input class from your CSS
                'placeholder':'Scientific name'

            }),

            'description': forms.Textarea(attrs={
                'class': 'description_input',  # Apply the text-input-description class from your CSS
                'placeholder':'Description'

            }),

            'usage_and_benefits': forms.Textarea(attrs={
                'class': 'usage_input',  # Apply the text-input-usage-benefit class from your CSS
                'placeholder':'Usage and benefits'

            }),

            'price': forms.TextInput(attrs={
                'class': 'price_input',  # Apply the text-input-price-field class from your CSS
                'placeholder':'Price'

            }),

            'quantity_available': forms.TextInput(attrs={
                'class': 'quantity_input'  # Apply the text-input-quantity-field class from your CSS
            }),

            'image': forms.FileInput(attrs={
                'class': 'image_input'
            })
        }

# class EditItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ('name','scientific_name', 'description', 'usage_and_benefits', 'price', 'quantity_available', 'image', 'is_sold')

#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'text-input'  # Apply the text-input class from your CSS
#             }),

#             'scientific_name': forms.TextInput(attrs={
#                 'class': 'text-input'  # Apply the text-input class from your CSS
#             }),

#             'description': forms.Textarea(attrs={
#                 'class': ''  # Apply the text-input-description class from your CSS
#             }),

#             'usage_and_benefits': forms.Textarea(attrs={
#                 'class': 'usage_benefit'  # Apply the text-input-usage-benefit class from your CSS
#             }),

#             'price': forms.TextInput(attrs={
#                 'class': ''  # Apply the text-input-price-field class from your CSS
#             }),

#             'quantity_available': forms.TextInput(attrs={
#                 'class': ''  # Apply the text-input-quantity-field class from your CSS
#             }),

#             'image': forms.FileInput(attrs={
#                 'class': 'image_input'
#             }),

#             'is_sold': forms.CheckboxInput(attrs={
#                 'class': 'form-checkbox h-5 w-5 text-teal-500'
#             }),
#         }
