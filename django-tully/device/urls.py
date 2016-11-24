from django.conf.urls import url, include

from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from device import views
from device.views import DataViewSet


router = DefaultRouter()
router.register(r'data', views.DataViewSet),

urlpatterns = [
    url(r'^$', views.DataViews.as_view(), name='datas_list'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
