from django.shortcuts import render
from django.http import HttpResponse
from . import invokeBashProcess as invoke
from .forms import ToolForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')


""" Network Tools View
# process the data in form.cleaned_data as required
# collects information from the forms POST request (stored as dict in django), and the feeds to the runTool Subprocess which runs the commands and displays its content
# re-render page with output:
"""
def network_tools(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():

            toolName = form.cleaned_data['tool']
            ipAddress = form.cleaned_data['ip_address']
            output = invoke.runTool(toolName,ipAddress)
            return render(request, 'tools/net_tools.html', {'output': output})#HttpResponse(f"Tool Results:\n{output}")
 
    else:
        #if the form is missing data returns a blank form
        form = ToolForm()
    return render(request, 'tools/net_tools.html', {'form': form})


"""
Below is some test views they are not accessible by the _sidebar but can be browed to using their respective links /testping, /testdig.
"""
def testping(request):
    output = invoke.runTool("ping","www.google.com")
    return HttpResponse(f"We Tried pinging google here is the result: {output}")

def testdig(request):
    output = invoke.runTool("dig","www.google.com")
    return HttpResponse(f"Dig of google: {output}") 
