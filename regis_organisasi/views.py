from django.shortcuts import render

# Create your views here.
def index(request):
    html='regis_organisasi/index.html'
    return render(request, html)
