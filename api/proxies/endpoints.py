from django.urls import re_path

from proxies.api import ProxiesAPI


urlpatterns = [
    re_path(r'^proxies/$', ProxiesAPI.as_view(), name='proxies'),
]
