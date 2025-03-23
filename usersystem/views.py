from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from .forms import RegisterForm, EditProfileForm, NewPasswordForm, EditUserProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from blogapp.models import UserProfile
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
class UserProfilePageView(DetailView):
    model = UserProfile
    template_name = 'user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfilePageView, self).get_context_data(*args, **kwargs)    # Use super to call the parent class get_context_data method(detail view).
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])                # Get the user profile object with the id from the URL. Kwarg = {'pk': id}
        context["page_user"] = page_user                                                # Add the user profile object to the context.
        return context                                                                  # Return the context dictionary.            

class EditProfilePageView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = UserProfile
    template_name = 'edit_profile_page.html'        # Set the template for the view.
    success_url = reverse_lazy('home')
    form_class = EditUserProfilePageForm            # Set the form class for the view. (In forms.py)

    def test_func(self):
        # Get the profile being edited
        profile = self.get_object()
        # Check if current user is the owner of the profile
        return self.request.user.id == profile.user.id

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to edit this profile.")
        return redirect('home')

    def get_success_url(self):
        # Redirect to the user's own profile page after successful edit
        return reverse_lazy('user_profile', kwargs={'pk': self.object.pk})


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
