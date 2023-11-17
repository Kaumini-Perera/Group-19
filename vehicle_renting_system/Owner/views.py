from django.shortcuts import render
from django.http import HttpResponse
from Owner.models import Owner
from Manager.models import Manager


# Create your views here.
def index(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    vehicle = Vehicle.objects.all()
    Message="Welcome Aboard!!"
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Owner_index.html',{'vehicle':vehicle,'Message':Message,'owner':owner,'no_of_pending_request':no_of_pending_request})

def Profile(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,'Owner_Profile.html',{'owner':owner,'no_of_pending_request':no_of_pending_request})

def register_manager(request):
    if('user_email' not in request.session):
        return redirect('/signin/')
    owner_email = request.session.get('user_email')
    owner = Owner.objects.get(Owner_email=owner_email)
    no_of_pending_request=count_pending_rent_request()
    return render(request,'register_manager.html',{'owner':owner,'no_of_pending_request':no_of_pending_request})
