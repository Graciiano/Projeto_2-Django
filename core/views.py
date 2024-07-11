from django.shortcuts import render
from django.contrib import messages
from core.forms import Contato, ProdutoModelForm
from .models import Produto
from django.shortcuts import redirect



def index(request):
    context = {
        'produtos': Produto.objects.all()
        
    }
    return render(request, 'index.html', context)

def contato(request):

    form = Contato(request.POST or None)
    
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'E-mail Enviado com sucesso')
            form =  Contato()
        else:
            messages.error(request, 'Erro ao enviar o email')
            
    
    context = {
        'form': form,
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
            
                form.save()
            
                messages.success(request, 'Produto salvo com sucesso.')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Error ao salvar o produto.')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
            
        return render(request, 'produto.html', context)
    else:
        return redirect('index')
