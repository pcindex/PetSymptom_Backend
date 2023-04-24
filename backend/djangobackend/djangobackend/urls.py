"""djangobackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from api.views import AppointmentView, Appointment_OfferView , ConditionsView, ExamView, SymptomsView, VerterinarianView 
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

#This file routes the urls of the backend, it is split into two sections, urls that are members of the router and everything else
#The router handles all api requests, while JWT authorization and BERT queries are routed seperately.
#

router = routers.DefaultRouter()
router.register(r'accounts', views.AccountView, basename='accounts')
router.register(r'pet_owners', views.Pet_OwnerView, basename='pet_owners')
router.register(r'pets', views.PetsView)
router.register(r'appointment_offers', Appointment_OfferView, basename='appointent_offers')
router.register(r'veterinarians', VerterinarianView, basename='veterinarians')
router.register(r'appointments', AppointmentView, basename='appointments')
router.register(r'exams', ExamView)
router.register(r'conditions', ConditionsView)
router.register(r'symptoms', SymptomsView)
router.register(r'register', views.RegisterView, basename='register')
urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="obtain_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('machinelearning/', include('MachineLearning.urls')),
]
