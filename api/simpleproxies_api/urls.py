from django.contrib import admin
from django.urls import include, re_path

# from custom_db_logger import endpoints as logs
from proxies import endpoints as proxies

from utils.views import not_found


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    # re_path(r'^api/', include(logs)),
    re_path(r'^', include(proxies)),
]

handler404 = not_found
