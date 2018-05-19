from django.conf.urls import url
from .views import index, auth_login

app_name='login'

urlpatterns=[
    url(r'^$', index, name='index'),
    url(r'^auth-login', auth_login, name='auth-login')
]