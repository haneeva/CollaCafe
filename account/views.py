from django.shortcuts import render, redirect
from django.views import View
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import auth


# Sign Up View

class ViewSignup(View):

    def get(self, request):
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'signup.html', context)

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered')
            else:
                user = form.save()
                messages.success(request, 'Registration successful.')
                return redirect('account:login')

        context = {'form': form}
        return render(request, 'signup.html', context)


# Login View

class ViewLogin(View):

    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)

    def post(self, request):
        form = LoginForm(request=request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            print(f"Username: {username}, Password: {password}")

            # Authenticate user
            user = authenticate(username=username, password=password)

            print(f"Authenticated user: {user}")

            if user is not None:
                # Log in the user
                login(request, user)
                return redirect('main:main')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            # Form is invalid, errors will be shown in the template
            messages.error(request, 'Please correct the errors below.')

        context = {'form': form}
        return render(request, 'login.html', context)


class ViewLogout(View):

    def get(self, request):
        auth.logout(request)
        return redirect('main:main')
