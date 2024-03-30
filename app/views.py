from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import AuthenticationForm
from app.models import Filmes

def index(request):
    filmes = Filmes.objects \
        .order_by('-id')

    paginator = Paginator(filmes, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Filmes - '
    }

    return render(
        request,
        'app/index.html',
        context
    )

def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('app:index')

    filmes = Filmes.objects \
        .filter(
            Q(nome__icontains=search_value) |
            Q(data__icontains=search_value) 
        )\
        .order_by('-id')

    paginator = Paginator(filmes, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Busca - ',
        'search_value': search_value,
    }

    return render(
        request,
        'app/index.html',
        context
    )

def filme(request, filme_id):
    try:
        filme = Filmes.objects.get(pk=filme_id)
    except Filmes.DoesNotExist:
        messages.error(request, 'Filme não existente')
        return redirect('app:index')
        
    site_title = f'{filme.nome} -'

    context = {
        'filme': filme,
        'site_title': site_title
    }

    return render(
        request,
        'app/filme.html',
        context
    )

def infouser(request):
    user = request.user
    site_title = f'{user.username} - '

    context = {
        'app': user,
        'site_title': site_title
    }

    return render(
        request,
        'app/user.html',
        context
    )
