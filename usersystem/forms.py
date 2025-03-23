from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blogapp.models import UserProfile

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

class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

class NewPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=100, 
        label="Current Password", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})
    )
    new_password1 = forms.CharField(
        max_length=100, 
        label="New Password", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})
    )
    new_password2 = forms.CharField(
        max_length=100, 
        label="Confirm New Password", 
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})
    )

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']

class EditUserProfilePageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_pic', 'website_url', 'twitter_url', 'github_url', 'artstation_url', 'linkedin_url']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'website_url': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.URLInput(attrs={'class': 'form-control'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control'}),
            'artstation_url': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control'}),
        }