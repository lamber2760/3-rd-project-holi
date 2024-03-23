from django.shortcuts import render,redirect
from django.http import HttpResponse 


# Create your views here.
def homepage(request):
    return render(request,"home.html")
def aboutus(request):
    return render(request,"aboutus.html")
def contactusx(request):
    return render(request,"contactus.html")
def check_form(request):
    return render(request,"check_form.html")

