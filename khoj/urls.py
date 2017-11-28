from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),

    # for search
    url(r'^search/$', views.search, name="search"),
]