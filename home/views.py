from django.shortcuts import render
from django.http import HttpResponse
import requests
import os

def home(request):
    if request.method == 'POST':
        nome = request.POST.get('nomeUsuario')
        email = request.POST.get('emailUsuario')
        setor = request.POST.get('setorUsuario')
        suporte = request.POST.get('suporteUsuario')
        categoria = request.POST.get('categoriaUsuario')
        detalhe = request.POST.get('detalheUsuario')

        if not nome:
            return HttpResponse("Nome é obrigatório. Por favor retorne e adicione seu nome.")
        if not email:
            return HttpResponse("Email é obrigatório, por favor retorne e adicione.")
        if not setor:
            return HttpResponse("Setor é obrigatório, retorne e adicione.")
        if not suporte:
            return HttpResponse("Você precisa adicionar o tipo de suporte.")

        url = "https://api.brevo.com/v3/smtp/email"
        headers = {
            "accept": "application/json",
            "api-key": os.environ.get('BREVO_API_KEY'),
            "content-type": "application/json"
        }
        payload = {
            "sender": {"name": "Alumax TI", "email": "b030cd001@smtp-brevo.com"},
            "to": [
                {"email": "gabriel.mendonca@alumax.ind.br"},
                {"email": "gabrielalto308viol@gmail.com"}
            ],
            "subject": "Novo Chamado de TI",
            "textContent": f"Nome: {nome}\nEmail: {email}\nSetor: {setor}\nSuporte: {suporte}\nCategoria: {categoria}\nDetalhes: {detalhe}"
        }
        requests.post(url, json=payload, headers=headers)

        return render(request, 'obrigado.html')

    return render(request, 'index.html')