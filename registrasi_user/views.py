from django.shortcuts import render

# Create your views here.
def index(request):
    html = 'registrasi_user/index.html'
    context = {
        'role':'',
        'relawan':'relawan',
        'sponsor':'sponsor',
        'donatur':'donatur'
    }
    return render(request, html, context)

def regis_donatur(request):
    html = 'registrasi_user/donatur.html'
    context={
        'role':'donatur'
    }