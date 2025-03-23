from django import forms
from .models import Post, Category
from django_summernote.widgets import SummernoteWidget

# Cast the QuerySet to a list of tuples. Our tuple is (database value, human-readable value).
try:
    categories = list(Category.objects.values_list('name', 'name'))
except:
    categories = [('Uncategorized', 'Uncategorized')]


class PostForm(forms.ModelForm):            # ModelForm allows for creating form fields for our model.
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'category', 'summary', 'body', 'header_image']  

        # Widgets takes a python dictionary to define the attributes of the form fields.
        # Using form-control class from Bootstrap to style the form fields.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Browser tab title (Optional)'}),
            'category': forms.Select(choices=categories, attrs={'class': 'form-control'}),

            'summary': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter a brief summary of the post to be displayed on the feed (Optional)...',
                'rows': 4
            }),

            'body': SummernoteWidget(),
        }

class EditForm(forms.ModelForm):            # ModelForm allows for creating form fields for our model.
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'category', 'summary', 'body']  

        # Widgets takes a python dictionary to define the attributes of the form fields.
        # Using form-control class from Bootstrap to style the form fields.
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Browser tab title (Optional)'}),
            'category': forms.Select(choices=categories, attrs={'class': 'form-control'}),
            
            'summary': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter a brief summary of the post to be displayed on the feed...',
                'rows': 4
            }),

            'body': SummernoteWidget(),
        }