from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegisterForm, EditProfileForm, NewPasswordForm
from django.contrib.auth.views import PasswordChangeView

# Create your views here.
class UserRegistrationView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')                 # Redirect to login after successful registration.

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')                  # Redirect to home after updating the profile.

    def get_object(self):                               # Return the currente user object to the view.
        return self.request.user
    
class PasswordsChangeView(PasswordChangeView):
    form_class = NewPasswordForm
    success_url = reverse_lazy('password_success')      # Redirect to password_success after changing the password.

def password_success(request):
    return render(request, 'registration/password_success.html', {})
