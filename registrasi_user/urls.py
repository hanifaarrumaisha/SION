from django.conf.urls import url
from .views import index, regis_donatur

urlpatterns=[
    url(r'^$', index, name='index'),
    url(r'^donatur', regis_donatur, name='regis_donatur' )
]