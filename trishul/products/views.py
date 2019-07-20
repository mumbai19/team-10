from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import (ListView, DetailView)
from .models import Product
# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

class ProductDetailView(DetailView):
    
    template_name = 'products/detail.html'
    def get_object(self):
        
        id_ = self.kwargs.get("id")
        return get_object_or_404(Products,id=id_)
