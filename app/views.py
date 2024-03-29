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

# Create your views here.
