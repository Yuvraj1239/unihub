from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
import logging
from django.contrib.auth.models import User
logger = logging.getLogger(__name__)


def create_user_manually(username, email, password):
    # Create a new User instance
    user = User.objects.create_user(username=username, email=email)

    # Set the password securely
    user.set_password(password)

    # Save the user object
    user.save()

    return user
def signup_view(request):
    # if request.method == 'POST':
    #     form = CustomUserCreationForm(request.POST)
    #     if form.is_valid():
    #         try:
    #             user = form.save()
    #             login(request, user)
    #             return redirect('events:list')
    #         except Exception as e:
    #             logger.error(f"Error during signup: {e}")
    #             form.add_error(None, "An error occurred during signup.")
    #     else:
    #         logger.error(f"Signup form invalid: {form.errors}")
    # else:
    #     form = CustomUserCreationForm()
    # return render(request, 'accounts/signup.html', {'form': form})
    user = create_user_manually("yuvraj","yurajchopra2001@gmail.com","Yuvrajchopra2001")
    login(request,user)
    return redirect('event:list')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = form.get_user()
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('events:list')
            except Exception as e:
                logger.error(f"Error during login: {e}")
                form.add_error(None, "An error occurred during login.")
        else:
            logger.error(f"Login form invalid: {form.errors}")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        try:
            logout(request)
        except Exception as e:
            logger.error(f"Error during logout: {e}")
        return redirect('events:list')
