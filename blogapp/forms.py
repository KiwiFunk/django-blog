from django import forms
from .models import Post

class PostForm(forms.ModelForm):            #ModelForm allows for creating form fields for our model.
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author', 'summary', 'body']  

        # Using form-control class from Bootstrap to style the form fields.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Browser tab title (Optional)'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a brief summary of the post'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your post here...'}),
        }