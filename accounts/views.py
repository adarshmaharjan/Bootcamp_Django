from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, SignUpForm

from django.contrib.auth import get_user_model
# from django.contrib.auth.middleware import AuthenticationMiddleware
# from django.contrib.auth.models import User

# Create your views here.

USER = get_user_model()


def login_view(request):
    if request.method == 'POST':
        # print(request.POST)
        form = LoginForm(request.POST)

        if form.is_valid():
            #ok and Login
            # print(form.cleaned_data)

            user = authenticate(
                username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            print(form.cleaned_data)
            if user:
                print('User is not found', user)
                login(request, user)
                return redirect('/accounts/profile')
            else:
                print('auth credentials don\'t match')
        else:
            pass
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/accounts/profile')
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context=context)


@login_required()
def profile_view(request):

    return render(request, 'accounts/profile.html')


def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            # print('Form is Valid')
            # print(form.cleaned_data)
            user = USER(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password'],

            )
            user.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/accounts/login/')
    elif request.method == 'GET':
        form = SignUpForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/signup.html', context=context)
