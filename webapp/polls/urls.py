from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:id_page>/', views.detail, name= 'detail'),
    path('<int:id_page>/results/', views.results, name= 'results'),
    path('<int:id_page>/vote/', views.vote, name= 'vote'),
] 
