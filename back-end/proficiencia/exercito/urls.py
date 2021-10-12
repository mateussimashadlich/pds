from django.urls import path

from . import views

urlpatterns = [
    path('paises', views.paises),
    path('paises/<int:id>', views.pais),
    path('paises/continentes', views.continentes),
    path('pessoas', views.pessoas),    
    path('pessoas/<int:id>', views.pessoa),
    path('pessoas/nao_militares', views.pessoas_nao_militares),
    path('exercitos', views.exercitos),
    path('militares', views.militares),
    path('militares/patentes', views.patentes),
    path('militares/<int:id>', views.militares),
    path('batalhoes', views.batalhoes),
    path('batalhoes/<int:id>', views.batalhao),
]
