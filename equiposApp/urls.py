from django.urls import re_path as url   
from equiposApp import views

urlpatterns = [
    url(r'^api/equipos$', views.equipos_list),
    url(r'^api/equipos/(?P<pk>[0-9]+)$', views.equipos_detail),
]
