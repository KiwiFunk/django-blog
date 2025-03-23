from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse_lazy
from .forms import RegisterForm, EditProfileForm, NewPasswordForm
from django.contrib.auth.views import PasswordChangeView
from blogapp.models import UserProfile

# Create your views here.
class UserProfilePageView(DetailView):
    model = UserProfile
    template_name = 'user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfilePageView, self).get_context_data(*args, **kwargs)    # Use super to call the parent class get_context_data method(detail view).
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])                # Get the user profile object with the id from the URL. Kwarg = {'pk': id}
        context["page_user"] = page_user                                                # Add the user profile object to the context.
        return context                                                                  # Return the context dictionary.            

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
