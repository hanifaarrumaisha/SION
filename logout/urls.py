from django.conf.urls import url
from .views import index

app_name='logout'

urlpatterns = [
    url(r'^$', index, name='index')
]