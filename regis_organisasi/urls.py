from django.conf.urls import url
from .views import index, regis_donatur, regis_relawan, regis_sponsor

app_name='regis_organisasi'

urlpatterns=[
    url(r'^$', index, name='index')
]
