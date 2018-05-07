from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    html='profil_organisasi/profil_organisasi.html'
    return render(request, html)
