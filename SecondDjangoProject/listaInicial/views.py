from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def paginaInicial(request):
    return HttpResponse(u"<html><body>Hello</body></html>")