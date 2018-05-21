from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def index(request):
    print ("#==> auth logout")
    request.session['islogout']=True
    
    messages.info(request, "Anda berhasil logout. Semua session Anda sudah dihapus")
    return HttpResponseRedirect(reverse('login:auth-login'))