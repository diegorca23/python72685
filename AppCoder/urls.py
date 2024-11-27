from django.urls import path

from AppCoder.views import listar_cursos

urlpatterns = [
     path('cursos/', listar_cursos),
]