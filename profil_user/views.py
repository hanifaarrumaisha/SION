from django.shortcuts import render
from django.contrib import messages

response={}
# Create your views here.
def index(request):
    response={
		'role':request.session['role'],
		'relawan':'relawan',
		'sponsor':'sponsor',
		'donatur':'donatur'
	}
	
    html='fitur4.html'
    return render(request, html, response)
