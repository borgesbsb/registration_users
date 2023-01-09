from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    nome_da_empresa = "Study with python"
    descricao = "Estudo de reciclagem de desenvolvimento de sistemas"
    contato_empresa = {
         "endereco": "Rua 03, numero 06, Vila Marinho, Compensa 3 - Manaus/AM",
         "telefone": "92982472705",
         "email": "borgesbsb.dev@gmail.com"
    }
    return render(request,'index.html', {'nome_empresa': nome_da_empresa,'descricao':descricao, 'contato_empresa':contato_empresa} )

def about(request):
    return HttpResponse("Pagina sobre")

def contact(request, id):
    return HttpResponse(id)
 