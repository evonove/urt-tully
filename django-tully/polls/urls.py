from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.datas_list, name='datas_list'),
]
