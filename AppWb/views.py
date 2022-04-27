from django.http import HttpResponse
from django.shortcuts import render

from AppWb.models import Empleados

# Create your views here.
def empleados(self):
    empleados = Empleados(nombre='pedro', grupo=40, fechaDeRegistro='2006-03-20', salario=40000, email='pedro@yopmail.com')
    empleados.save()
    documentdoDtxt = f'nombre: {empleados.nombre}, Grupo: {empleados.grupo}, Fecha de registro: {empleados.fechaDeRegistro}, Salario: {empleados.salario}, Email: {empleados.email}'
    return HttpResponse(documentdoDtxt)