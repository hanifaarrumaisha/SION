from django.shortcuts import render

# Create your views here.
def index(request):
	#USER DETEKSI SIAPA YG LOGIN
	#AMBIL ROLE
	#CARI DIA DITABLE ROLE ITU PAKE 
    html='fitur4.html'
    return render(request, html)
