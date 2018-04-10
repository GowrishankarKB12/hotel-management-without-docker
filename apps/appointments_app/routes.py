from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^book$', views.book),
    url(r'^login$', views.login),
    url(r'^finish$', views.finish),
    url(r'^reservation$', views.reservation),
    url(r'^back$', views.back),
]
