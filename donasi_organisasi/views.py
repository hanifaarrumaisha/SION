from django.shortcuts import render
from django.db import connection


# Create your views here.
#def index(request):
	#html='donasi_organisasi/donasi_organisasi.html'
	#return render(request, html)


response={}
def index(request):
	cur = connection.cursor()		
	cur.execute('SET SEARCH_PATH to SION;')
	cur.execute('SELECT * FROM ORGANISASI')
	response['organisasi'] = dictfetchall(cur)
	print(response['organisasi'])
	html='donasi_organisasi/donasi_organisasi.html'
	return render(request, html, response)


def dictfetchall(cursor):
  
	columns = [col[0] for col in cursor.description]
	return [
		dict(zip(columns, row))
		for row in cursor.fetchall()
	]

#response={}
#@csrf_protect
#def donasi_organisasi_post(request):
 #   if(request.method == 'POST'):
  #  	response['organisasi'] = request.POST['organisasi']
   # 	response['jumlah_dana'] = request.POST['jumlah_dana']

#		cur=connection.cursor()
#
 #   	cur.execute('SELECT count(*) FROM ORGANISASI WHERE email_organisasi=%s AND nama=%s',(response['email'], response['nama']))
  #  	all = cur.fetchone() # (5,) [(lila,) (imel,)]
   # 	if (all[0] == 0):
    #		cur.execute('INSERT INTO ORGANISASI (email_organisasi,website,nama,provinsi,kabupaten_kota,kecamatan,kelurahan,kode_pos,status_verifikasi) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',(response['email'],response['web'],response['nama'],response['prov'],response['kab'],response['kec'],response['jln'],response['kodepos'],'terverifikasi'))
    #		cur.execute('INSERT INTO "USER" (email, password, nama, alamat_lengkap) values (%s, %s, %s, %s)',(response['email_pengurus'], 'abc123', response['nama_pengurus'], response['alamat_pengurus']))
    #		cur.execute('INSERT INTO PENGURUS_ORGANISASI (email, organisasi) values (%s,%s)',(response['email_pengurus'],response['email']))
    #		connection.commit()
    #		html ='fitur3.5.html'
    #		return render(request, html, response)
    #	else:
    #		html ='fitur3.5 gagal verifikasi.html'
    #		return render(request, html, response)
    #
    #else:        
     #   return HttpResponseRedirect('/login/')


#def donate(request):
#	 user={}
 #   if request.method == "POST":
