from django.conf.urls import url
from accounts.views import register



app_name='accounts'

urlpatterns=[
    url(r'login/',register, name='register'),
]
