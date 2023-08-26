from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from app_login.models import Cadastro
from django.contrib.auth.hashers import make_password

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')


def cadastrar_usu(request): 
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        # Verifica se a senha é válida
        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'preencha todos os campos!')
            if senha != senha():
                messages.add_message(request, constants.ERROR, ' senha nao sao igueis')
            
            return redirect('/cadastro/')
        

   
    novo_usuario = Cadastro(nome_usuario=nome, email_usuario=email, senha=senha)
    novo_usuario.save()

    cadastrar_usu = {
        'cadastrar_usu' : Cadastro.objects.all()
    }

    return render(request,'login.html')

            
def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        try:
            cadastro = Cadastro.objects.get(email_usuario=email)
        except Cadastro.DoesNotExist:
            # O usuário com este email não existe
            return HttpResponse('O usuário com este email não existe')
        else:
            # O usuário com este email existe
            if cadastro.senha == senha:
                # A senha está correta
                return HttpResponse('Você está logado!')
            else:
                # A senha está incorreta
                return HttpResponse('Senha incorreta')
    else:
        return HttpResponse('Método de solicitação inválido')

    