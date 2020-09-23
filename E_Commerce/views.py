from django.shortcuts import render
from .models import *
from math import ceil


def homepage(request):
    homeslider = HomeSlider.objects.all()

    # Top Product
    topprod = TopProducts.objects.all()
    menprod = MenProducts.objects.all()
    prodcards = ProdCard.objects.all()

    return render(request, 'E_Commerce/home.html', {'homeslider': homeslider, 'topprod': topprod,
                                                    'prodcard': prodcards, 'menprod': menprod})


def customersignupform(request):
    message1 = "Thank you for using our Service. Please Signup below."
    return render(request, 'E_Commerce/CustomerSignUp.html',{'message1':message1})


def customersignup(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        mail = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        if password_confirmation == password:
            signup_form = CustomerSignUp()
            signup_form.UserName = user_name
            signup_form.usermail = mail
            signup_form.userpass = password
            signup_form.save()
            message1 = "Account Created Successfully!!"
            return render(request, 'E_Commerce/CustomerSignUp.html', {'message1':message1})
        else:
            message1 = "Ooopsss! Passwords are not matched. Please Try Again with Same Passwords."
            return render(request, 'E_Commerce/CustomerSignUp.html', {'message1': message1})
    return render(request, 'E_Commerce/home.html')

def signIn(request):
    customer_data = CustomerSignUp.objects.all().values()
    specialOffers = SpecialOffers.objects.all()
    if request.method == 'POST':
        usermail = request.POST.get('email')
        userpass = request.POST.get('password')
        for data in customer_data:
            if data['usermail'] == usermail and data['userpass']== userpass:
                message = "Special Offer for our authenticated Users."
                return render(request, 'E_Commerce/Sigin_Valid.html', {'message1':message,
                                                                       'specialoffer':specialOffers})
        else:
            message = "Invalid! Seems like you do not have an account! Please Sign Up below"
            return render(request, 'E_Commerce/CustomerSignUp.html', {"message1": message})

def specialoffer(request, offerid):
    specialproduct = SpecialOffers.objects.filter(id=offerid)
    qty = range(1,30)
    return render(request, 'E_Commerce/SpecialOffers.html', {'special': specialproduct[0], 'Qty':qty})

#####################################
"""
        Admin Panel 
Hassam
hassam@gmail.com
programmer

"""
