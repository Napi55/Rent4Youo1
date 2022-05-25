from django.urls import path
from . import views
from .views import list


urlpatterns = [
    path('accueil/', views.page_accueil),
    path('list/', views.page_accueil),
    path('offre/', views.offre),
    path('signature/', views.page_accueil),
    path('', list.as_view(), name='list')

]