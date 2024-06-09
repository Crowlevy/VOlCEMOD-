from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_db
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from hashlib import sha256
from django.contrib import messages, auth
from django.contrib.messages import constants

def register(request):
    if request.method == "GET":
        return render(request,'usuarios/registerUser.html')
    else:
        username = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if User.objects.filter(email = email).exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse email')
            return redirect('/register/')

        if User.objects.filter(username = username).exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome')
            return redirect('/register/')

        try:

            usuario = User.objects.create_user(username = username, email = email, password = senha)
            usuario.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')
            return redirect('/Angola_Hub/')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/register/')

    
def login(request):
    if request.method == "GET":
        return render(request,'usuarios/loginUser.html')
    else:
        username = request.POST.get('nome')
        senha = request.POST.get('senha')
    
        usuario = auth.authenticate(username=username, password = senha)
    print(usuario)
    if not usuario:
        messages.add_message(request, constants.WARNING, 'Nome ou senha inválidos')
        return redirect('/login/')    
    else:
        auth.login(request, usuario)
        return redirect('/Angola_Hub')

        
@login_required(login_url="/login")
def Angola_Hub(request):
    return render(request,'main/index.html')

