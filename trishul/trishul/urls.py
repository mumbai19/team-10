"""trishul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views, settings
from django.contrib import admin
from .views import home_page, donate,checkout,payments
from .views import home_page, donate,cart
from accounts.views import register, user_login, user_logout
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
urlpatterns = ([
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_page, name='home'),
    url(r'^donate/', donate, name='donate'),
    url(r'^register', register, name='register'),
    url(r'^login', user_login, name='login'),
    url(r'^logout/', user_logout, name='logout'),
    url(r'^products/', include('products.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^checkout/',checkout,name='checkout'),
    url(r'^payments/',payments,name='payments'),
    url(r'^cart/',cart,name='cart'),
])+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
