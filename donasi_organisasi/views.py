from django.shortcuts import render

# Create your views here.
def index(request):
    html='donasi_organisasi/donasi_organisasi.html'
    return render(request, html)
