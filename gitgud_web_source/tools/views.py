from django.shortcuts import render
from django.http import HttpResponse
from . import invokeBashProcess as invoke
# Create your views here.

def index(request):
    return HttpResponse(f"Hello, world. You're at the tools page index.")

def ping(request):
    output = invoke.runTool("ping","-c4 -q www.google.com")
    return HttpResponse(f"We Tried pinging google here is the result:\n{output}")

def dig(request):
    output = invoke.runTool("dig","www.google.com")
    return HttpResponse(f"Dig of google:\n{output}")

def mtr(reqeust):
    output= invoke.runTool("mtr", "-rzc15 -s100 www.google.com")
    return HttpResponse(f"MTR of google:\n{output}")