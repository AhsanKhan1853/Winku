from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account created successfully for {username}!')  # Added this line to display success message.
            return redirect('/')
        return render(request, 'register.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, "You have been successfully logged out!")
    return redirect('/')


class LoginViewWithMessage(auth_views.LoginView):
    success_message = "You have been successfully logged in."
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in! Logg Out First")
            return redirect('home')  # Redirect to your index page
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response


@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
        return render(request, 'index.html', {'form': p_form})
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html',context)



@login_required
def edit_profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')
        return render(request, 'index.html', {'form': p_form})
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'edit-profile-basic.html',context)



# This is a class-based view for updating user's profile.

# class ProfileUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
#     model = Profile
#     fields = ['image', 'bio', 'gender']
#     template_name = 'profile.html'
#     success_message = "Your profile has been updated successfully."