from django.shortcuts import render
from accounts.forms import UserForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


def register(request):
    registered = False
    if request.method=='POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    dict = {'user_form':user_form, 'registered':registered}
    return render(request, 'accounts/register.html', dict)

@login_required
def special(request):
    return HttpResponse('You are logged in')

def user_login(request):
    print('Inuser')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print('Login attempt unsuccessful')
            print('{} and {}'.format(username, password))
            return HttpResponse('Invalid credentials')
    else:
        return render(request, 'accounts/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
