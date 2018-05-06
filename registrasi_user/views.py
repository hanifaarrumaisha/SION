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
    html = 'registrasi_user/index.html'
    context={
        'role':'Donatur',
        'relawan':'Relawan',
        'sponsor':'Sponsor',
        'donatur':'Donatur'
    }
    return render(request, html, context)

def regis_sponsor(request):
    html = 'registrasi_user/index.html'
    context={
        'role':'Sponsor',
        'relawan':'Relawan',
        'sponsor':'Sponsor',
        'donatur':'Donatur'
    }
    return render(request, html, context)

def regis_relawan(request):
    html = 'registrasi_user/index.html'
    context={
        'role':'Relawan',
        'relawan':'Relawan',
        'sponsor':'Sponsor',
        'donatur':'Donatur'
    }
    return render(request, html, context)