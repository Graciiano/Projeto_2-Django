from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto


class Contato(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem',widget=forms.Textarea())
    
    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']
        
        conteudo = f'nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
        
        mail = EmailMessage(
            subject= 'E-mail enviado pelo sistema Django',
            body=conteudo,
            from_email='diogodev00@gmail.com',
            to=['diogodev00@gmail.com'],
            headers={'Reply-To': email}
        )
        mail.send()
        

class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']