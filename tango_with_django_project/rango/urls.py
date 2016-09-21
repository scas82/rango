from django.conf.urls import url
from rango import views

urlpatterns = [
    url('^$', views.index, name='index')
]
