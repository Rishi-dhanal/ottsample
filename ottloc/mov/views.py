from datetime import timedelta
import datetime
from profile import Profile

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
# Create your views here.
from django.shortcuts import render, redirect
from .form import RegistrationForm, UserProfileForm, LoginForm

# views.py

from django.shortcuts import render

from .models import Movie, Register, Membership

def ott_home_view(request):
    return render(request, 'home.html')

def register_user(request):
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            # Redirect to a success page after registration
            return redirect('login')  # Replace 'success_url' with your success URL name
    else:
        registration_form = RegistrationForm()

    return render(request, 'user/registration.html', {'registration_form': registration_form})


def login_user(request):
    error_message = None

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            try:
                user = Register.objects.get(username=username)
                if user.password == password:
                    # Login successful, redirect to 'home.html'
                    return render(request, 'account/welcome.html')  # Redirect to the home page
                else:
                    # Password mismatch
                    error_message = 'Invalid username or password.'
            except Register.DoesNotExist:
                # User does not exist
                error_message = 'Invalid username or password.'
        else:
            error_message = 'Invalid form data. Please check the entered values.'
    else:
        login_form = LoginForm()

    return render(request, 'account/login.html', {'login_form': login_form, 'error_message': error_message})

def membership(user, plan):
    
    start_date = datetime.now().date()

    if plan == 'basic':
        end_date = start_date + timedelta(days=30)  # Basic membership for 30 days
        amount = 10.00  # Replace with your basic membership amount
    elif plan == 'premium':
        end_date = start_date + timedelta(days=90)  # Premium membership for 90 days
        amount = 25.00  # Replace with your premium membership amount
    elif plan == 'vip':
        end_date = start_date + timedelta(days=365)  # VIP membership for 1 year
        amount = 100.00  # Replace with your VIP membership amount
    else:
        return None  # Return None if an invalid plan is provided

    membership = Membership.objects.create(
        user=user,
        start_date=start_date,
        end_date=end_date,
        amount=amount
    )
    return membership

def select_user_type(request):
    return render(request, 'select_user_type.html')

def adult_user_page(request):
    # Retrieve the logged-in user
    current_user = request.user

    # Get the user's profile if it exists
    try:
        user_profile = current_user.profile  # Assuming a OneToOneField relation with Profile model
    except Profile.DoesNotExist:
        user_profile = None

    return render(request, 'adult_user_page.html', {'user_profile': user_profile})

def child_user_page(request):
    # Logic for child user page
    return render(request, 'child_user_page.html')

def create_new_profile(request):
    # Logic to create a new profile
    # For example, create a new entry in your database

    # Return a JSON response indicating success
    return JsonResponse({'success': True})