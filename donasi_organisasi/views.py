from django.shortcuts import render
from django.db import connection
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib import messages


# Create your views here.
#def index(request):
	#html='donasi_organisasi/donasi_organisasi.html'
	#return render(request, html)


response={}
def index(request):
  cur = connection.cursor()		
  cur.execute('SELECT * FROM ORGANISASI')
  response['organisasi'] = dictfetchall(cur)
  html='donasi_organisasi/donasi_organisasi.html'
  response['roles'] =request.session['role']
  print(response['roles'])
  return render(request, html, response)


def dictfetchall(cursor):
  columns = [col[0] for col in cursor.description]
  return [
    dict(zip(columns, row))
    for row in cursor.fetchall()
  ]

response={}
@csrf_protect
def donasi_organisasi_post(request):
    response={
      'role':request.session['role'],
      'relawan':'relawan',
      'sponsor':'sponsor',
      'donatur':'donatur',
      'pengurus':'pengurus'
    }
    print('MASUK')
    if(request.method == 'POST'):
      organisasi = request.POST['organisasi']
      print(organisasi)
      jumlah_dana = request.POST['jumlah_dana']
      print(jumlah_dana)

      cur=connection.cursor()
      user = request.session['user']
      if (request.session['role']=='sponsor'):
        if(jumlah_dana < 2000000):
            messages.error(request, "Jumlah dana minimal adalah Rp2000.000")
        else:
           cur.execute ('SELECT so.nominal FROM SPONSOR_ORGANISASI so, ORGANISASI o WHERE so.sponsor = %s AND o.nama = organisasi );',(user.email))
           getNominal = cur.fetchall()
           print(getNominal)
           newNominal = getNominal + jumlah_dana
           cur.execute ('UPDATE SPONSOR_ORGANISASI SET nominal = newNominal WHERE sponsor = %s);', (user.email))

    return HttpResponseRedirect(reverse('donasi-organisasi:index'))

