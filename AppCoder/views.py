from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

from AppCoder.models import Cursos


# Create your views here.

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def otra_vista(request):
    return HttpResponse("<h1>¡Esto es un título!</h1><p>Y este es un párrafo.</p>")

def dia_de_hoy(request):
    hoy = date.today()
    return HttpResponse(f"Hoy es {hoy}")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido a Coder")

def probando_template(request, nombre):
    hoy = date.today()
    listaDeNotas = [10, 1, 5, 3, 9]
    return render(request, "AppCoder/prueba.html", {'nom':nombre, "fecha": hoy, 'notas':listaDeNotas} )

def listar_cursos(request):
    cursos = Cursos.objects.all()

    return render(request, "AppCoder/lista_cursos.html", {"cursos": cursos})