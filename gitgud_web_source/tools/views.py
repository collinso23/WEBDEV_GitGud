from django.shortcuts import render
from django.http import HttpResponse
from . import invokeBashProcess as invoke
from .forms import ToolForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return(request, 'login.html')

def pingpage(request):
    return render(request,'tools/pingpage.html' ) #HttpResponse(f"Hello, world. You're at the tools page index.")

def network_tools(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            toolName = form.cleaned_data['tool']
            ipAddress = form.cleaned_data['ip_address']
            results = invoke.runTool(toolName,ipAddress)
            return render(request, 'tools/net_tools.html', {'results': results})#HttpResponse(f"Tool Results:\n{output}")
 
    else:
        form = ToolForm()

    return render(request, 'tools/net_tools.html', {'form': form})


def test_form(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            toolName = form.cleaned_data['tool']
            ipAddress = form.cleaned_data['ip_address']
            results = invoke.runTool(toolName,ipAddress)
            return render(request, 'tools/test_form.html', {'results': results})#HttpResponse(f"Tool Results:\n{output}")
 
    else:
        form = ToolForm()

    return render(request, 'tools/test_form.html', {'form': form})

def testping(request):
    output = invoke.runTool("ping","www.google.com")
    return HttpResponse(f"We Tried pinging google here is the result: {output}")

def testdig(request):
    output = invoke.runTool("dig","www.google.com")
    return HttpResponse(f"Dig of google: {output}") 
