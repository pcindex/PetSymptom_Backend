from msilib.schema import Condition

from django.http import Http404
from api.models import *
from rest_framework.views import APIView
from rest_framework import viewsets, permissions, response
from rest_framework.decorators import action
from api.serializers import *

#This file contains the api endpoint views. These methods are named to correlate with their respective 
#URL endpoints and serializers. 
#The views are built on the ModelViewSet class. These with with a range of baked in options listed here https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset 
#"queryset" Provides information as to what information the user will retrieve with a GET from the endpoint.
#the base variable references the instances of defined models in "Models.py"
#"permission_classes" dictates what kind of users can access the given endpoint
#"serializer_class" lets the view know what method to use to serialize the expected data



class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class AccountView(viewsets.ModelViewSet):
    queryset = Account.objects.all().order_by('email')
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

class Pet_OwnerView(viewsets.ModelViewSet):
    queryset = Pet_Owner.objects.all().order_by('user_id')
    serializer_class = Pet_OwnerSerializer
    permission_classes = [permissions.IsAuthenticated]


##DEPRECIATED

#class DogView(viewsets.ModelViewSet):
#    queryset = Dog.objects.all().order_by('breed')
#    serializer_class = DogSerializer
#    permission_classes = [permissions.AllowAny]
#
#class CatView(viewsets.ModelViewSet):
#    queryset = Cat.objects.all().order_by('breed')
#    serializer_class = CatSerializer
#    permission_classes = [permissions.AllowAny]

class PetsView(viewsets.ModelViewSet):
    queryset = Pets.objects.all().order_by('owner')
    serializer_class = PetsSerializer
    permission_classes = [permissions.IsAuthenticated]

class Appointment_OfferView(viewsets.ModelViewSet):
    queryset = Appointment_Offer.objects.all().order_by("offer_id")
    serializer_class = Appointment_OfferSerializer
    permission_classes = [permissions.IsAuthenticated]


class VerterinarianView(viewsets.ModelViewSet):
    queryset = Veterinarian.objects.all().order_by("vet_id")
    serializer_class = VerterinarianSerializer
    permission_classes = [permissions.IsAuthenticated]

   

class AppointmentView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('appointment_id')
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExamView(viewsets.ModelViewSet):
    queryset = Exam.objects.all().order_by("exam_id")
    serializer_class = ExamSerializer
    permission_classes = [permissions.IsAuthenticated]

class ConditionsView(viewsets.ModelViewSet):
    queryset = Conditions.objects.all().order_by("condition_id")
    serializer_class = ConditionsSerializer
    permission_classes = [permissions.IsAuthenticated]

class SymptomsView(viewsets.ModelViewSet):
    queryset = Symptoms.objects.all().order_by("symptom_id")
    serializer_class = SymptomsSerializer
    permission_classes = [permissions.IsAuthenticated]
