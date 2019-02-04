from django.urls import path
from fichasManage import views


urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'fichas/', views.fichas_campo_todas, name='fichas_campo_todas'),
    path(r'fichas/<int:ficha_id>', views.ficha_campo_detail, name='ficha_campo_detail'),
]

