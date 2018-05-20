from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, csrf_exempt

cur=connection.cursor()

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

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

def regis_user(request, email, password, name, alamat):
    print("masuk regis user")
    # try:
    
    isValid=True
    cur.execute('SELECT * FROM "USER" WHERE password=%s AND email IN (SELECT email FROM SPONSOR WHERE email=%s);', (password, email))
    getUser=dictfetchall(cur)
    if(getUser):
        user=getUser[0]
        isValid=False
        messages.error(request, "Username dan Password sudah ada")

    if (isValid & (password!="") & (alamat!="")):
        cur.execute("""INSERT INTO "USER" (email, password, nama, alamat_lengkap) VALUES(%s,%s,%s,%s)""", (email, password, name, alamat))
        connection.commit()
        print("commit regis")
        cur.execute('SELECT * FROM "USER" WHERE nama=%s', (email))
        print(cur.fetchone())
    else:
        messages.error(request, "Input tidak boleh ada yang kosong")
    # except Exception as e:
    #     messages.error(request, "Input tidak benar")

@csrf_protect
def regis_donatur(request):
    email=''
    print("masuk regis_donatur")
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        nama = request.POST['name']
        alamat=request.POST['alamat']+', '+request.POST['kecamatan']+', '+request.POST['kabupaten']+", "+request.POST['provinsi']+", "+request.POST['kodepos']
        
        regis_user(request, email, password, nama, alamat) 

        cur.execute('INSERT INTO DONATUR (email, saldo) VALUES(%s,0)', (email))
        connection.commit()
        
        cur.execute('SELECT * FROM DONATUR WHERE email=%s', (email))

        request.session['user']=cur.fetchone()
        request.session['role']='donatur'

        messages.success(request, "Selamat! Kamu berhasil mendaftar.")
    return HttpResponseRedirect(reverse('login:auth-login'))
            
