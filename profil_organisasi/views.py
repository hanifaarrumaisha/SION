from django.shortcuts import render
from django.db import connection

# Create your views here.
# Create your views here.
response={}
def index(request):
	cur = connection.cursor()		
	#cur.execute('SET SEARCH_PATH to SION;')
	cur.execute('SELECT * FROM ORGANISASI O JOIN TUJUAN_ORGANISASI TU ON O.email_organisasi = TU.organisasi ')
	
	response={
		'role':request.session['role'],
        'relawan':'relawan',
        'sponsor':'sponsor',
        'donatur':'donatur',
		'pengurus':'pengurus'
	}
	response['organisasi'] = dictfetchall(cur)
	cur.execute(' SELECT po.EMAIL, po.ORGANISASI FROM PENGURUS_ORGANISASI po, ORGANISASI o WHERE o.email_organisasi = po.organisasi')
	response['pengurus_org']=dictfetchall(cur)

	cur.execute(' SELECT d.donatur, d.organisasi FROM DONATUR_ORGANISASI d, ORGANISASI o WHERE o.email_organisasi = d.organisasi')
	response['donatur_org']=dictfetchall(cur)

	cur.execute('SELECT s.sponsor, s.organisasi FROM SPONSOR_ORGANISASI s, ORGANISASI o WHERE o.email_organisasi = s.organisasi')
	response['sponsor_org']=dictfetchall(cur)

	cur.execute('SELECT s.organisasi, SUM(s.nominal) FROM SPONSOR_ORGANISASI s, ORGANISASI o WHERE o.email_organisasi = s.organisasi GROUP BY organisasi')
	response['donasi_sponsor']=dictfetchall(cur)

	print(response['donasi_sponsor'])
	html='profil_organisasi/profil_organisasi.html'
	return render(request, html, response)


def dictfetchall(cursor):
  
	columns = [col[0] for col in cursor.description]
	return [
		dict(zip(columns, row))
		for row in cursor.fetchall()
	]


#SELECT organisasi, SUM(nominal)
#FROM DONATUR_ORGANISASI
#GROUP BY organisasi

#SELECT EMAIL
##FROM PENGURUS_ORGANISASI po, ORGANISASI o
#WHERE o.email_organisasi = po.organisasi;



	



