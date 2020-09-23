from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='Home Page'),
    path('signIn', views.signIn, name='signIn'),
    path('SignUpform', views.customersignupform, name='Customer Sign Up form'),
    path('CustomerSignUp', views.customersignup, name='Customer Sign Up'),
    path('SpecialOffers/<int:offerid>', views.specialoffer, name='Special Offer'),
]