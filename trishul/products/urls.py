from django.conf.urls import url
from products.views import ProductListView

app_name='products'

urlpatterns=[
    url(r'^$', ProductListView.as_view(), name='list'),
]
