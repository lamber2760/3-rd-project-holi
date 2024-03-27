from django.shortcuts import render,redirect
from django.http import HttpResponse 
from holi.models import form


# Create your views here.
def homepage(request):
    return render(request,"home.html")
def aboutus(request):
    return render(request,"aboutus.html")
def formx(request):
    return render(request,"form.html")
def check_form(request):
    return render(request,"check_form.html")
def savethis(request):
    if request.method =="POST":
        fullname=request.POST.get("fname")
        useremail=request.POST.get("email")
        phonenumber=request.POST.get("number")
        message=request.POST.get("msg")
        myimg=request.FILES.get('img')
        myemail=f"""
    """
