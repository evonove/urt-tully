from django.conf.urls import url, include
from device import views
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('device.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
