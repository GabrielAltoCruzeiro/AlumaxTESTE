from django.shortcuts import render
from django.http import HttpResponse 
from django.core.mail import send_mail

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

        send_mail(
            subject="Novo Chamado de TI",
            message=f"""
            Nome: {nome}
            Email: {email}
            Setor: {setor}
            Suporte: {suporte}
            Categoria: {categoria}
            Detalhes: {detalhe}
            """,
            from_email="gabrielalto.tech@outlook.com",
            recipient_list=["gabriel.mendonca@alumax.ind.br", "gabrielalto308viol@gmail.com"],
            fail_silently=False,
        )

        return render(request, 'obrigado.html')

    return render(request, 'index.html')
    