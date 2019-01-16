from django.urls import path
from fichasManage import views


urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'fichas/', views.fichas_campo_todas, name='fichas_campo_todas'),
    path(r'estructuras/', views.estructuras_geologicas_todas, name='estructuras_geologicas_todas'),
]

