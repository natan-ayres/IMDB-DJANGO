from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms import RegisterForm, RegisterUpdateForm
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada!')
            return redirect('app:login')


    return render(
        request,
        'app/register.html',
        {
            'form': form
        }
    )

def loginview(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request,'Logado com sucesso! ')
            return redirect('app:index')
        messages.error(request, 'Login invalido')
    
    return render(
        request,
        'app/login.html',
        {
            'form': form
        }
    )

def logoutview(request):
    auth.logout(request)
    return redirect('app:login')

def updateview(request):
    form = RegisterUpdateForm(instance=request.user)
    
    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)   
         
        if form.is_valid():
            form.save()
            form = AuthenticationForm(request, data=request.POST)
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Atualizado com sucesso! ')
            return redirect('app:index')

    return render(
        request,
        'app/register.html',
        {
            'form': form
        }
    )

def deleteview(request):
    user = request.user
    user.delete()
    messages.success(request, 'Usuário Deletado')
    return redirect('app:login')