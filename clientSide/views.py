from django.shortcuts import render


def page_accueil(request):
    return render(request, 'rent4you/Page_accueil.html', context={})


def list(request):
    return render(request, 'rent4you/list.html', context={})


def offre(request):
    return render(request, 'rent4you/offre.html', context={})


def signature(request):
    return render(request, 'rent4you/signature.html', context={})