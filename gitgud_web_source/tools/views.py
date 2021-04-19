from django.shortcuts import render
from django.http import HttpResponse
from . import invokeBashProcess as invoke
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return(request, 'login.html')
    
def dashboard(request):
    return render(request, 'tools/base.html')

def network_tools(request):
    return render(request,'tools/pingpage.html' ) #HttpResponse(f"Hello, world. You're at the tools page index.")

def test_form(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    else:
        form = NameForm()

    return render(request, 'tools/nettools.html', {'form': form})

def testping(request):
    output = invoke.runTool("ping","www.google.com")
    return HttpResponse(f"We Tried pinging google here is the result: {output}")

def testdig(request):
    output = invoke.runTool("dig","www.google.com")
    return HttpResponse(f"Dig of google: {output}") 
