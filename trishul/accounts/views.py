# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import requests
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, FormView, DetailView, UpdateView
from django.utils.http import is_safe_url
from django.contrib.auth import authenticate, login, get_user_model
from .forms import LoginForm, RegisterForm, GuestForm, UserDetailChangeForm
from .models import GuestDetails
from .signals import user_logged_in
from ecommerce.mixins import NextUrlMixin, RequestFormAttachMixin

class LoginView(NextUrlMixin, RequestFormAttachMixin, FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    sucess_url = '/'
    default_next = '/'

    def form_valid(self, form):
        next_path = self.get_next_url()
        return redirect(next_path)


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {'form':form,}
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        print(form.cleaned_data)
        email = form.cleaned_data.get('email')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        mobile_number = form.cleaned_data.get('mobile_number')
        new_guest_email = GuestDetails.objects.create(email= email,first_name=first_name, last_name=last_name, mobile_number=mobile_number)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            return redirect(redirect_path)
        else:
            return redirect('/register/')
    return redirect('/register/')





