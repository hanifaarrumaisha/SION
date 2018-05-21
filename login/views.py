from django.shortcuts import render
from django.db import connection
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# Create your views here.
def index(request):
    if 'user' in request.session:
        return HttpResponseRedirect(reverse('profil-user:index'))
    else:
        html='login/index.html'
        return render(request, html)

@csrf_exempt
def auth_login(request):
    user={}
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']

        cur=connection.cursor()
        isValid=False

        print("masuk")
        # Cek for Sponsor 
        cur.execute('SELECT * FROM "USER" WHERE password=%s AND email IN (SELECT email FROM SPONSOR WHERE email=%s);', (password, username))
        getUser=dictfetchall(cur)
        if(getUser):
            user=getUser[0]
            request.session['role']='sponsor'
            isValid=True

        # Cek for donatur 
        if not(isValid):
            cur.execute('SELECT * FROM "USER" WHERE password=%s AND email IN (SELECT email FROM DONATUR WHERE email=%s);', (password, username))
            getUser=dictfetchall(cur)

            if(getUser):
                user=getUser[0]
                request.session['role']='donatur'
                isValid=True

        # Cek for relawan 
        if not(isValid):
            cur.execute('SELECT * FROM "USER" WHERE password=%s AND email IN (SELECT email FROM RELAWAN WHERE email=%s);', (password, username))
            print(cur.fetchone())
            getUser=dictfetchall(cur)
            print("relawan")
            print(getUser)
            if(getUser):
                user=getUser[0]
                request.session['role']='relawan'
                isValid=True
    
        # Cek for pengurus 
        if not(isValid):
            cur.execute('SELECT * FROM "USER" WHERE password=%s AND email IN (SELECT email FROM pengurus_organisasi WHERE email=%s);', (password, username))
            getUser=dictfetchall(cur)
            if(getUser):
                user=getUser[0]
                request.session['role']='pengurus'
                isValid=True

        if not(isValid):
            messages.error(request, "Username atau password salah")
        else:
            request.session['user'] = user
            print(request.session['user'])
            messages.success(request, "Anda berhasil login")
    return HttpResponseRedirect(reverse('login:index'))
