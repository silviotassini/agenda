from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def cadastro(request):
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    usuario = request.POST.get('usuario')
    senha2 = request.POST.get('senha2')
    print(request.POST)
    if not nome or not sobrenome or not email or not usuario or not senha :
        messages.error(request, "Nenhum campo pode ser vazio")
        return render(request, 'accounts/cadastro.html')    
    try:
        validate_email(email)
    except:
        messages.error(request, "E-mail inválido")
        return render(request, 'accounts/cadastro.html') 
    if len(senha)<6 :
        messages.error(request, "Senha precisa ter ao menos 6 caracteres")
        return render(request, 'accounts/cadastro.html')     
    if senha != senha2 :
        messages.error(request, "Senhas não são iguais")
        return render(request, 'accounts/cadastro.html')        
    if len(usuario)<6 :
        messages.error(request, "Nome usuario  precisa ter ao menos 6 caracteres")
        return render(request, 'accounts/cadastro.html')   

    if User.objects.filter(username=usuario).exists():
        messages.error(request, "Usuário  já existe")
        return render(request, 'accounts/cadastro.html')   

    user = User.objects.create_user(username=usuario, email=email, password=senha, first_name=nome,last_name=sobrenome)
    user.save()
    messages.success(request, 'Sucesso')
    return redirect('login')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')