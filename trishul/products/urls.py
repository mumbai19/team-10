from django.conf.urls import url
from products.views import ProductListView,ProductDetailView

app_name='products'

urlpatterns=[
    url(r'', ProductListView.as_view(), name='list'),
    url(r'<int:id>/', ProductDetailView.as_view(), name='detail'),

]
