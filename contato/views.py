from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import FormContato



def contatoView(request):
    send = False

    form = FormContato(request.POST or None)
    if form.is_valid():
        #enviar e-mail
        nome = request.POST.get('nome','')
        email = request.POST.get('email','')
        mensagem = request.POST.get('mensagem','')
        email = EmailMessage(
            "Mensagem dos Reinos de Ferro",
            "De {} <{}> Escreveu: \n\n{}".format(nome,email,mensagem),
            "nao-responder@inbox.mailtrap.io",
            ["carlosalbertoprojetos2020@gmail.com"],
            reply_to=[email]     
        )
        try:
            email.send()
            send = True
        except:
            send = False       

    context = {
        'form':form,
        'success':send
    }
    return render(request,'contato/contato.html',context)   

