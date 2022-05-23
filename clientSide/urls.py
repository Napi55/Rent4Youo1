from django.urls import path
from . import views


urlpatterns = [
    path('accueil/', views.page_accueil),
    path('list/', views.page_accueil),
    path('offre/', views.page_accueil),
    path('signature/', views.page_accueil),

]