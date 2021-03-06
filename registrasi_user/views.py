from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from datetime import date

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

def insert_user(email, password, name, alamat):
        if ((password!="") & (alamat!="") & (name!="")):
            query= 'INSERT INTO "USER" (email, password, nama, alamat_lengkap) VALUES(%s,%s,%s,%s)'
            data= (email, password, name, alamat)
            cur.execute(query, data)
            print("commit regis")
            query='SELECT * FROM "USER" WHERE email=%s'
            data=(email,)
            cur.execute(query, data)
            print(cur.fetchone())
        else:
            messages.error(request, "Input tidak boleh ada yang kosong")

def regis_user(request, email):
    print("masuk regis user")
    # try:
    
    isValid=True
    # cur.execute('SELECT * FROM "USER"')
    # print(cur.fetchall())
    query='SELECT * FROM "USER" WHERE email=%s'
    data=(email,)
    cur.execute(query, data)
    getUser=dictfetchall(cur)
    print(getUser)
    
    if (len(getUser)!=0):
        print("masuk false")
        user=getUser[0]
        isValid=False
        messages.error(request, "Tidak dapat menggunakan username tersebut")
    return isValid

@csrf_protect
def regis_donatur(request):
    print("masuk regis_donatur")
    if request.method == 'POST':
        print("masuk post")
        email=request.POST['email']
        password=request.POST['password']
        nama = request.POST['name']
        alamat=request.POST['alamat']+', '+request.POST['kecamatan']+', '+request.POST['kabupaten']+", "+request.POST['provinsi']+", "+request.POST['kodepos']

        if (regis_user(request, email)): 
            query = 'SELECT * FROM "USER" WHERE email IN (SELECT email FROM DONATUR WHERE email=%s)'
            data = (email, )
            cur.execute(query, data)
            getUser=dictfetchall(cur)
            print("donatur udah ada: ",getUser)
            if (len(getUser)!=0):
                print("masuk false")
                user=getUser[0]
                messages.error(request, "Tidak dapat menggunakan username tersebut")

            else:
                insert_user(email, password, nama, alamat)
                connection.commit()
                query = 'INSERT INTO DONATUR (email, saldo) VALUES(%s,0)'
                data = (email,)
                cur.execute(query, data)
                connection.commit()
                
                query='SELECT * FROM DONATUR WHERE email=%s'
                cur.execute(query, data)

                request.session['user']=dictfetchall(cur)
                print(request.session['user'])
                request.session['role']='donatur'

                messages.success(request, "Selamat! Kamu berhasil mendaftar.")
                return HttpResponseRedirect(reverse('login:auth-login'))
    return HttpResponseRedirect(reverse('registrasi-user:form-donatur'))

@csrf_exempt
def regis_sponsor(request):
    print("----> Masuk regis_sponsor")
    if request.method == 'POST':
        print("masuk post")
        email=request.POST['email']
        password=request.POST['password']
        nama = request.POST['name']
        alamat=request.POST['alamat']+', '+request.POST['kecamatan']+', '+request.POST['kabupaten']+", "+request.POST['provinsi']+", "+request.POST['kodepos']
        logo=request.POST['logo']

        isValid=regis_user(request, email)

        if (isValid & (logo!="")): 
            query = 'SELECT * FROM "USER" WHERE email IN (SELECT email FROM SPONSOR WHERE email=%s)'
            data = (email, )
            cur.execute(query, data)
            getUser=dictfetchall(cur)
            print("sponsor udah ada: ",getUser)
            if (len(getUser)!=0):
                print("masuk false")
                user=getUser[0]
                messages.error(request, "Tidak dapat menggunakan username tersebut")

            else:
                insert_user(email, password, nama, alamat)
                connection.commit()
                query = 'INSERT INTO SPONSOR (email, logo_sponsor) VALUES(%s, %s)'
                data = (email, logo)
                cur.execute(query, data)
                connection.commit()

                query='SELECT * FROM SPONSOR WHERE email=%s'
                data=(email,)
                cur.execute(query, data)

                request.session['user']=dictfetchall(cur)
                print(request.session['user'])
                request.session['role']='sponsor'

                messages.success(request, "Selamat! Kamu berhasil mendaftar.")
                return HttpResponseRedirect(reverse('login:auth-login'))
        elif not(isValid):
            return HttpResponseRedirect(reverse('registrasi-user:form-sponsor'))
        
        messages.error(request,'Gak boleh ada field yang kosong yaa')
        return HttpResponseRedirect(reverse('registrasi-user:form-sponsor'))

@csrf_exempt
def regis_relawan(request):
    print("----> Masuk regis_relawan")
    if request.method == 'POST':
        print("masuk post")
        email=request.POST['email']
        password=request.POST['password']
        nama = request.POST['name']
        alamat=request.POST['alamat']+', '+request.POST['kecamatan']+', '+request.POST['kabupaten']+", "+request.POST['provinsi']+", "+request.POST['kodepos']
        nohp=request.POST['nohp']
        ttl=request.POST['ttl']
        keahlian=request.POST['keahlian']
        print(type(ttl))
        
        isValid=regis_user(request, email)

        if ( isValid & (nohp!="") & (ttl!="") & (keahlian!="")): 
            query = 'SELECT * FROM "USER" WHERE email IN (SELECT email FROM RELAWAN WHERE email=%s)'
            data = (email, )
            cur.execute(query, data)
            getUser=dictfetchall(cur)
            print("sponsor udah ada: ",getUser)
            if(len(getUser)!=0):
                print("masuk false")
                user=getUser[0]
                messages.error(request, "Tidak dapat menggunakan username tersebut")

            else:
                insert_user(email, password, nama, alamat)
                query = 'INSERT INTO RELAWAN (email, no_hp, tanggal_lahir) VALUES(%s, %s, %s)'
                data = (email, nohp, ttl)
                cur.execute(query, data)
                connection.commit()
                query = 'INSERT INTO KEAHLIAN_RELAWAN (email, keahlian) VALUES(%s, %s)'
                data = (email, keahlian)
                cur.execute(query, data)
                connection.commit()
                print("masuk relawan commit")
                
                query='SELECT * FROM RELAWAN WHERE email=%s'
                data=(email,)
                cur.execute(query, data)
                user = dictfetchall(cur)[0]
                user['tanggal_lahir']=user.get('tanggal_lahir').isoformat()
                request.session['user']=user
                print("blabla ", request.session['user'])
                request.session['role']='relawan'

                messages.success(request, "Selamat! Kamu berhasil mendaftar.")

                return HttpResponseRedirect(reverse('login:auth-login'))
            return HttpResponseRedirect(reverse('registrasi-user:form-relawan'))
        elif not(isValid):        
            return HttpResponseRedirect(reverse('registrasi-user:form-relawan'))
        else:
            messages.error(request,'Gak boleh ada field yang kosong yaa')
            return HttpResponseRedirect(reverse('registrasi-user:form-relawan'))