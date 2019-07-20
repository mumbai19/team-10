from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, get_user_model

def home_page(request):
    return render(request, 'index.html')
