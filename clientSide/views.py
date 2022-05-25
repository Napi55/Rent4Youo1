from django.shortcuts import render
from django.template import context

from .models import Véhicule
from  .filters import VéhiculeFilter
from  django.views.generic import ListView


def page_accueil(request):
    véhicule = Véhicule.objects.all()
    return render(request, 'rent4you/Page_accueil.html', context={'véhicule': véhicule})


def list(request):
    véhicule = Véhicule.objects.all()
    myFilter = VéhiculeFilter(request.GET, queryset=véhicule)
    #véhicule=myFilter.qs
    return render(request, 'rent4you/list.html', context={'véhicule': véhicule, 'myFilter':myFilter})


class list(ListView):
    model = Véhicule
    template_name = 'rent4you/list.html'
    context_object_name = 'véhicule'

    def get_context_data(self, *, object_list=None, **kwargs):
        search_input = self.request.GET.get('search-area')or ''
        #if search_input:
            #context['véhicule'] = context['véhicule'].filter(location=search_input)
        #return context







def offre(request):
    return render(request, 'rent4you/offre.html', context={})


def signature(request):
    return render(request, 'rent4you/signature.html', context={})