from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index ,name='index'),
    #/gallery/3/
    url(r'^(?P<albumId>[0-9]+)/$', views.details,name='details')
]