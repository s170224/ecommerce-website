from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib import messages
from Apps.useraccount.models import *
from Apps.women.models import *
from Apps.shoppingitems.models import *



# Create your views here.


def home(request):
    userdata = CustomUser.objects.all()

    print('Fetched user data:', userdata)


    for user in userdata:
        print(user)

    return render(request, 'home/home.html', {'user_profiles': userdata})

def women_data_view(request):
    womendata = Womendress.objects.all()
    print("woe", womendata)

    return render(request,'home/women.html', {'womendress_data': womendata})

def user_data_view(request):
    userdata = CustomUser.objects.all()


    return render(request,'home/user.html', {'userdata': userdata})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)

        if user is not None:
            # print('userkavya',user)
            login(request,user)
            return redirect('Home')
        else:
            messages.error(request, "Invalid username or password.")
            print("Invalid username or password.")
    return render(request,'login.html')


def women_items_data_view(request,id):
    print("vvvv",id)

    women_items_data = WomenDresesItems.objects.filter(category=id)


    print('women',women_items_data)
    return render(request, 'home/womendresses.html', {'women_items_data' : women_items_data})





