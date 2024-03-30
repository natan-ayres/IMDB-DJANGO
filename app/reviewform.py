from typing import Any, Dict
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from app.models import Reviews
from django.urls import reverse
from app.forms import ReviewForm

def create(request):
    form_action = reverse('app:create')

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            review = form.save(commit=False)
            review.usuario = request.user
            review.save()
            messages.success(request, 'Review Criada')
            return redirect('app:userinfo')

        return render(
            request,
            'app/create.html',
            context
        )

    context = {
        'form': ReviewForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'app/review.html',
        context
    )

def update(request, review_id):
    try:
        review = Reviews.objects.get(pk=review_id)
    except review.DoesNotExist:
        messages.error(request, 'Review não existente')
        return redirect('app:index')
    if review.usuario == request.user:
        form_action = reverse('app:update', args=(review_id,))

        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)

            context = {
                'form': form,
                'form_action': form_action,
            }

            if form.is_valid():
                review = form.save()
                messages.success(request, 'Review Atualizado')
                return redirect('app:userinfo')

            return render(
                request,
                'app/review.html',
                context
            )

        context = {
            'form': ReviewForm(instance=review),
            'form_action': form_action,
        }

        return render(
            request,
            'app/review.html',
            context
        )
    else:
        messages.error(request, 'Você não é o Owner dessa review')
        return redirect('app:index')

def delete(request, review_id):
    review = review.objects.get(pk=review_id)
    if review.usuario == request.user:
        review.delete()
        messages.success(request, 'Review Deletado')
        return redirect('app:index')
    else:
        messages.error(request, 'Você não é o Owner dessa review')
        return redirect('app:index')