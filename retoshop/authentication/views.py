from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from .forms import RegisterForm
import random
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']
            
            # Authenticate user
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                
                # If remember_me is False, set session to expire when browser closes
                if not remember_me:
                    request.session.set_expiry(0)
                
                return redirect('store.html')  # Redirect to a store page after successful login
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account until email is verified
            user.set_password(form.cleaned_data['password'])  # Set hashed password
            user.save()

            # Generate OTP
            otp = random.randint(1000, 9999)

            # Save OTP to session
            request.session['otp'] = otp
            request.session['user_id'] = user.id

            # Send OTP to the user's email
            send_mail(
                'Your OTP for Email Verification',
                f'Your OTP is {otp}',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )

            return redirect('verify_otp')  # Redirect to OTP verification page
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})





def verify(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        otp = request.session.get('otp')
        user_id = request.session.get('user_id')

        if int(entered_otp) == otp:
            user = User.objects.get(id=user_id)
            user.is_active = True  # Activate the user account
            user.save()
            login(request, user)
            del request.session['otp']  # Clear OTP from session
            return redirect('home')  # Redirect to homepage after successful verification
        else:
            return render(request, 'verify.html', {'error': 'Invalid OTP. Please try again.'})

    return render(request, 'verify.html')
