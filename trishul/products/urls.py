from django.conf.urls import url
from products.views import (ProductListView, ProductBagsListView, ProductBookmarksListView,
                            ProductCardsListView, ProductJewelleryListView, ProductPaperweightsListView,
                            ProductKeychainsListView, ProductCandlesListView)

app_name='products'

urlpatterns=[
<<<<<<< HEAD
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^bags/', ProductBagsListView.as_view(), name='bags'),
    url(r'^bookmarks/', ProductBookmarksListView.as_view(), name='bookmarks'),
    url(r'^cards/', ProductCardsListView.as_view(), name='cards'),
    url(r'^jewellery/', ProductJewelleryListView.as_view(), name='jewellery'),
    url(r'^keychain/', ProductKeychainsListView.as_view(), name='keychains'),
    url(r'^paperweights/', ProductPaperweightsListView.as_view(), name='paperweights'),
    url(r'^candles/', ProductCandlesListView.as_view(), name='candles'),

=======
    url(r'', ProductListView.as_view(), name='list'),
>>>>>>> f7418790d69847895a22b162e0496b7391061c6a
]
