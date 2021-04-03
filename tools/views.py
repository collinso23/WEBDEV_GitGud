from django.shortcuts import render
from django.http import HttpResponse
from . import invokeBashProcess as invoke
# Create your views here.

def index(request):
    output=invoke.pingTool("www.google.com")
    return HttpResponse(f"Hello, world. You're at the tools page index.\n\nWe Tried pinging google here is the result\n{output}")
