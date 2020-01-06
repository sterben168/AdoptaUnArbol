from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^arboles/$', views.VistaArboles.as_view(), name='arboles'),
    url(r'^arbol/(?P<pk>\d+)$', views.DetallesArboles.as_view(), name='detalles-arbol'),
    url(r'^personas/$', views.VistaPersonas.as_view(), name='personas'),
    url(r'^persona/(?P<pk>\d+)$', views.DetallesPersonas.as_view(), name='detalles-persona'),

]
