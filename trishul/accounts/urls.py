from django.conf.urls import url
from accounts import views

app_name = 'accounts'

urlpatterns=[
    url('^register/', views.register, name='register'),
    url('^login/', views.user_login, name='login'),
]
