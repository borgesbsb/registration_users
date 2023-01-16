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
    
    cursos_home = {
        1: {"titulo": "Django Fundamentos","descricao": "Aprenda toda a base do Django agora mesmo!!"},
        2: {"titulo": "Flask Fundamentos","descricao": "Aprenda toda a base do Flask agora mesmo!!"},
        3: {"titulo": "Python OO","descricao": "Aprenda orientação a objetos com python"}
    }
    return render(request,'index.html', {'nome_empresa': nome_da_empresa,'descricao':descricao, 'contato_empresa':contato_empresa, 'cursos_home':cursos_home, } )

def about(request):
    return render(request,'empresa/about.html')

def contact(request, id):
    return render(request,'empresa/contact.html')
 