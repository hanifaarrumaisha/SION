from django.conf.urls import url
from .views import index

app_name='profil_user'

urlpatterns=[
    url(r'^$', index, name='index')
]
