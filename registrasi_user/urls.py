from django.conf.urls import url
from .views import index, regis_donatur, regis_relawan, regis_sponsor

app_name='registrasi_user'

urlpatterns=[
    url(r'^$', index, name='index'),
    url(r'^donatur', regis_donatur, name='regis-donatur'),
    url(r'^sponsor', regis_sponsor, name='regis-sponsor'),
    url(r'^relawan', regis_relawan, name='regis-relawan')
]