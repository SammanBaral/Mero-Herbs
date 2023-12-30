from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'w-full py-2 px-4 rounded-xl border focus:outline-none focus:border-blue-500','id':'comment_text'}),
        }