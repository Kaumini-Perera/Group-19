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


def ManagerRegistration(request):
    Manager_firstname = request.POST.get('Manager_firstname', '')
    Manager_lastname = request.POST.get('Manager_lastname', '')
    Manager_dob = request.POST.get('Manager_dob', '')
    Manager_gender = request.POST.get('Manager_gender', '')
    Manager_mobileno = request.POST.get('Manager_mobileno', '')
    Manager_email = request.POST.get('Manager_email', '')
    Manager_password = request.POST.get('Manager_password', '')
    Manager_address = request.POST.get('Manager_address', '')
    Manager_city = request.POST.get('Manager_city', '')
    Manager_state = request.POST.get('Manager_state', '')
    Manager_country = request.POST.get('Manager_country', '')
    Manager_pincode = request.POST.get('Manager_pincode', '')
    Manager_license = request.FILES['Manager_license']

    result_customer = Customer.objects.filter(customer_email=Manager_email)
    result_owner = Owner.objects.filter(Owner_email=Manager_email)
    result_manager = Manager.objects.filter(Manager_email=Manager_email)
    if result_customer.exists() or result_owner.exists() or result_manager.exists():
        Message = "This Email address already exist!!"
        return render(request, 'register_manager.html', {'Message': Message})
    else:
        manager = Manager(Manager_firstname=Manager_firstname, Manager_lastname=Manager_lastname,
                          Manager_dob=Manager_dob, Manager_gender=Manager_gender, Manager_mobileno=Manager_mobileno,
                          Manager_email=Manager_email, Manager_password=Manager_password,
                          Manager_address=Manager_address,
                          Manager_city=Manager_city, Manager_state=Manager_state, Manager_country=Manager_country,
                          Manager_pincode=Manager_pincode, Manager_license=Manager_license)

        manager.save()
        return redirect('/Owner/AllManagers')