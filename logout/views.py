from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    print ("#==> auth logout")
    request.session.flush() # menghapus semua session
    
    messages.info(request, "Anda berhasil logout. Semua session Anda sudah dihapus")
    return HttpResponseRedirect(reverse('login:index'))