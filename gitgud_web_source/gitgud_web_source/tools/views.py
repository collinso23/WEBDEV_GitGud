from django.shortcuts import render
from django.http import HttpResponse
from . import invokeBashProcess as invoke
# Create your views here.

def index(request):
    return HttpResponse(f"Hello, world. You're at the tools page index.")


def pingpage(request):
    output = invoke.runTool("ping","www.google.com")
    return HttpResponse(f"We Tried pinging google here is the result: {output}")

def digpage(request):
    output = invoke.runTool("dig","www.google.com")
    return HttpResponse(f"Dig of google: {output}") 
