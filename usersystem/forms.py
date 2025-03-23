from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):                                    # This method is called when the form is initialized.
        super(RegisterForm, self).__init__(*args, **kwargs)                 # Call the parent class's __init__() method.

        self.fields['username'].widget.attrs['class'] = 'form-control'      # Add a CSS class to the predefined fields.
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'