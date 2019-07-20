from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView, DetailView, View
from .models import Product
# Create your views here.

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

class ProductBagsListView(ListView):
    template_name = 'products/list.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductBagsListView, self).get_context_data(*args,**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.bags()

class ProductJewelleryListView(ListView):
    template_name = 'products/list.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductJewelleryListView, self).get_context_data(*args,**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.jewellery()

class ProductKeychainsListView(ListView):
    template_name = 'products/list.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductKeychainsListView, self).get_context_data(*args,**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.keychains()

class ProductBookmarksListView(ListView):
    template_name = 'products/list.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductBookmarksListView, self).get_context_data(*args,**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.bookmarks()

class ProductCardsListView(ListView):
    template_name = 'products/list.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductCardsListView, self).get_context_data(*args,**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.cards()

class ProductCandlesListView(ListView):
    template_name = 'products/list.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductCandlesListView, self).get_context_data(*args,**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.candles()

class ProductPaperweightsListView(ListView):
    template_name = 'products/list.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductPaperweightsListView, self).get_context_data(*args,**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.paperweights()
