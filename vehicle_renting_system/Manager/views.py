from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from Owner.models import Owner
from Manager.models import Manager
from CustomerHome.models import Customer
from Vehicles.models import Vehicle
from RentVehicle.models import RentVehicle

from datetime import datetime
from datetime import date

# Create your views here.
def index(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    vehicle = Vehicle.objects.all()
    Message="Welcome Aboard!!"
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Manager_index.html',{'vehicle':vehicle,'Message':Message,'manager':manager,'no_of_pending_request':no_of_pending_request})

def Profile(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Manager_Profile.html',{'manager':manager,'no_of_pending_request':no_of_pending_request})

def AllCustomers(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    customer = Customer.objects.all()
    no_of_pending_request=count_pending_rent_request()
    return render(request,"Manager_All_Customers.html",{'customer':customer,'manager':manager,'no_of_pending_request':no_of_pending_request})

def Customer_Profile(request,customer_email):
    if('user_email' not in request.session):
        return redirect('/signin/')
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    customer = Customer.objects.get(customer_email=customer_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Manager_Customer_Profile.html',{'manager':manager,'customer':customer,'no_of_pending_request':no_of_pending_request})

def upload_Vehicle(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,"Manager_Upload_Vehicle.html",{'manager':manager,'no_of_pending_request':no_of_pending_request})

def AllVehicles(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    vehicle = Vehicle.objects.all()
    no_of_pending_request=count_pending_rent_request()
    return render(request,"Manager_all_vehicles.html",{'vehicle':vehicle,'manager':manager,'no_of_pending_request':no_of_pending_request})

def showdetails(request,Vehicle_license_plate):
    if('user_email' not in request.session):
        return redirect('/signin/')
    vehicle = Vehicle.objects.get(Vehicle_license_plate=Vehicle_license_plate)
    manager_email = request.session.get('user_email')
    manager = Manager.objects.get(Manager_email=manager_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Manager_showdetails.html',{'vehicle':vehicle,'manager':manager,'no_of_pending_request':no_of_pending_request})

