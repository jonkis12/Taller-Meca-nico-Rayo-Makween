from django.db import router
from django.urls import path, include
from .views import lista_trabajos, detalle_trabajo, TrabajoViewSet
from rest_framework import routers

from rest_auto import views

router = routers.DefaultRouter()
router.register('trabajos/(?P<id>\d+)/?$', views.TrabajoViewSet)

trabajo_list = TrabajoViewSet.as_view({
    'get': 'list',
    'post': 'create'
    })
trabajo_detail = TrabajoViewSet.as_view({
    'get': 'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
    })


urlpatterns = [
    path('lista_trabajos',lista_trabajos,name="lista_trabajos"),
    path('detalle_trabajo/<id>',detalle_trabajo,name="detalle_trabajo"),
    path('r/', include(router.urls)),
    path('r/trabajo_list', trabajo_list),
    path('r/trabajo_list/<id>', trabajo_detail),
]