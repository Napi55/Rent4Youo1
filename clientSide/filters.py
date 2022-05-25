import django_filters
from .models import *

class VéhiculeFilter(django_filters.FilterSet):
    class Meta:
        models = Véhicule
        fields = ['disponibilité', ]




