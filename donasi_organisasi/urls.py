from django.conf.urls import url
from .views import index, donasi_organisasi_post

app_name='registrasi_user'

urlpatterns=[
    url(r'^$', index, name='index'),
    url(r'^donasi', donasi_organisasi_post, name='donasi_organisasi_post'),
]
