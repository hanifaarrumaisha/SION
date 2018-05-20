from django.conf.urls import url
from .views import index, form_donatur, form_relawan, form_sponsor, regis_donatur

app_name='registrasi_user'

urlpatterns=[
    url(r'^$', index, name='index'),
    url(r'^donatur', form_donatur, name='form-donatur'),
    url(r'^sponsor', form_sponsor, name='form-sponsor'),
    url(r'^relawan', form_relawan, name='form-relawan'),
    url(r'^regis-donatur', regis_donatur, name='regis-donatur'),
]