from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from datetime import date
from .models import User, Appointment
# Create your views here.


def index(request):
    return render(request, 'appointments_app/index.html')

def book(request):
    if request.method == 'GET':
        return redirect ('/reservation')
    newuser = User.objects.validate(request.POST)
    print (newuser)
    if newuser[0] == False:
        for each in newuser[1]:
            messages.error(request, each) 
        return redirect('/reservation')
    if newuser[0] == True:
        messages.success(request,'Thank you for the booking')
        return redirect('/reservation')

def login(request):
        return render(request, 'appointments_app/appointment.html')

def reservation(request):
        return render(request, 'appointments_app/updatetime.html')

def back(request):
        return render(request, 'appointments_app/index.html')


def finish(request):
    if request.method != "POST":
        messages.error(request,"Can't add like that!")
        return redirect('/login')
    else:
        add_appoint= Appointment.objects.finish(request.POST)
        return redirect('/')
