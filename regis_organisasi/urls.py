from django.conf.urls import url
from .views import index 

app_name='regis_organisasi'

urlpatterns=[
    url(r'^$', index, name='index')
]
