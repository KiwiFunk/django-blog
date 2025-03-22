from django import forms
from .models import Post

class PostForm(forms.ModelForm):            # ModelForm allows for creating form fields for our model.
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author', 'summary', 'body']  

        # Widgets takes a python dictionary to define the attributes of the form fields.
        # Using form-control class from Bootstrap to style the form fields.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Browser tab title (Optional)'}),
            'author': forms.Select(attrs={'class': 'form-control'}),

            'summary': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter a brief summary of the post to be displayed on the feed (Optional)...',
                'rows': 4
            }),

            'body': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Type your post here...',
                'rows': 14
            }),
        }

class EditForm(forms.ModelForm):            # ModelForm allows for creating form fields for our model.
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'summary', 'body']  

        # Widgets takes a python dictionary to define the attributes of the form fields.
        # Using form-control class from Bootstrap to style the form fields.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Browser tab title (Optional)'}),
            
            'summary': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter a brief summary of the post to be displayed on the feed...',
                'rows': 4
            }),

            'body': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Type your post here...',
                'rows': 14
            }),
        }