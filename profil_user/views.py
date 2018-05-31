from django.shortcuts import render
from django.contrib import messages

response={}
# Create your views here.
def index(request):
    if (request.session['first_view_profil']) :
        print("profil ", request.session['first_view_profil'])
        messages.info(request, "Anda berhasil login")
        request.session['first_view_profil']=False
    response={
		'role':request.session['role'],
		'relawan':'relawan',
		'sponsor':'sponsor',
		'donatur':'donatur'
	}
    html='fitur4.html'
    return render(request, html, response)
