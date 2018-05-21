from django.conf.urls import url
from .views import index, regis_organisasi_post

app_name = 'regis_organisasi'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^verifying', regis_organisasi_post, name='verifying')
]
