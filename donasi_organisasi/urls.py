from django.conf.urls import url
from .views import index

app_name='registrasi_user'

urlpatterns=[
    url(r'^$', index, name='index')
]
