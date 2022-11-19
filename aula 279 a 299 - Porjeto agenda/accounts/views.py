from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import FormContact


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    user = request.POST.get('user')
    password = request.POST.get('password')
    user = auth.authenticate(request, username=user, password=password)

    if not user:
        print('not user')
        messages.error(request, 'Invalid user or password.')
        return render(request, 'accounts/login.html')
    else:
        print('user validate')
        auth.login(request, user)
        messages.success(request, 'Successfully login!')
        return redirect('dashboard')


def logout(request):
    auth.logout(request)
    return redirect('index')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    name = request.POST.get('name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    user = request.POST.get('user')
    password = request.POST.get('password')
    confirm = request.POST.get('confirm')

    if not name or not last_name or not email or not user or not password or not confirm:
        messages.error(request, 'No field can be empty.')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Invalid email.')
        return render(request, 'accounts/register.html')

    if len(password) < 8:
        messages.error(request, 'Password is too short.')
        return render(request, 'accounts/register.html')

    if len(user) < 8:
        messages.error(request, 'User name is too short.')
        return render(request, 'accounts/register.html')

    if password != confirm:
        messages.error(request, 'Passwords do not match.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=user).exists():
        messages.error(request, 'This user already exists.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'This email already exists.')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Successfully registered. Now make login!')
    user = User.objects.create_user(username=user, email=email, password=password,
                                    first_name=name, last_name=last_name)
    user.save()
    return redirect('login')


@login_required(redirect_field_name='login')
def dashboard(request):
    if request.method != 'POST':
        form = FormContact()
        return render(request, 'accounts/dashboard.html', {'form': form})

    form = FormContact(request.POST, request.FILES)

    if not form.is_valid():
        messages.error(request, 'Error submitting form.')
        form = FormContact(request.POST)
        return render(request, 'accounts/dashboard.html', {'form': form})

    form.save()
    messages.success(request, f'Contact {request.POST.get("name")} was successfully saved in contact list')
    return redirect('dashboard')
