from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse

cur=connection.cursor()

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

def form_donatur(request):
    html = 'registrasi_user/index.html'
    context={
        'role':'Donatur',
        'relawan':'Relawan',
        'sponsor':'Sponsor',
        'donatur':'Donatur'
    }
    return render(request, html, context)

def form_sponsor(request):
    html = 'registrasi_user/index.html'
    context={
        'role':'Sponsor',
        'relawan':'Relawan',
        'sponsor':'Sponsor',
        'donatur':'Donatur'
    }
    return render(request, html, context)

def form_relawan(request):
    html = 'registrasi_user/index.html'
    context={
        'role':'Relawan',
        'relawan':'Relawan',
        'sponsor':'Sponsor',
        'donatur':'Donatur'
    }
    return render(request, html, context)

def regis_user(request):
    if request.method == 'POST':
        try:
            alamat=request.POST['alamat']+', '+request.POST['kecamatan']+', '+request.POST['kabupaten']+", "+request.POST['provinsi']+", "+request.POST['kodepos']
            cur.execute('INSERT INTO "USER" (email, password, nama, alamat_lengkap) VALUES(%s,%s,%s,%s)', (request.POST['email'], request.POST['password'], request.POST['name'], alamat))
            connection.commit()
            cur.execute('SELECT * FROM "USER" WHERE nama=%s', (request.POST['name']))
            print(cur.fetchone())
        except Exception as e:
            messages.error(request, "Input tidak benar")
            return

def regis_donatur(request):
    regis_user(request) 
    response={'role':'donatur'}
    return HttpResponseRedirect(reverse('login:auth-login'))
            
