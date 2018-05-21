from django.shortcuts import render

response={}
# Create your views here.
def index(request):
	#USER DETEKSI SIAPA YG LOGIN
	#AMBIL ROLE
	#CARI DIA DITABLE ROLE ITU PAKE 
	response={
		'role':request.session['role'],
        'relawan':'Relawan',
        'sponsor':'Sponsor',
        'donatur':'Donatur'
	}
	html='fitur4.html'
	return render(request, html, response)
