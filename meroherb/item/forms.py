from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'scientific_name', 'description', 'usage_and_benefits', 'price', 'quantity_available', 'image', )

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),

            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'scientific_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),

            'usage_and_benefits': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),

            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'quantity_available': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }