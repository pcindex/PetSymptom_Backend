from api.models import (Account, Pet_Owner, 
Pets, Veterinarian, Appointment_Offer, Appointment, Exam, Conditions, Symptoms 
)
from rest_framework import serializers
from django.contrib.auth.models import User

#This file defines the serializers for expected posts to each endpoint.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password','username')
        write_onlyfields = ('password')
#The User model contains extra information for password hashing, validation, and permission groups.
#Therefore it requires extra serialization
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('account_id', 'phone_number', 'email', 'city', 'state', 'zipcode','user')

    

class Pet_OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet_Owner
        fields = ('user_id', 'address')

#DEPRECIATED

#class DogSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Dog
#        fields = ("__all__")
#
#class CatSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Cat
#        fields = ('breed', 'declawed')

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ('pet_id', 'name', 'dob', 'reproductive_status', 'had_kids', 'weight', 'height', 'age', 'conditions', 'owner')

class Appointment_OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment_Offer
        fields = ('offer_id', 'owner', 'pet_id', 'date', 'activeRequest','symptoms_id') 

class VerterinarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinarian
        fields = ('vet_id', 'name')

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('appointment_id', 'owner', 'pet_id','vet_id', 'location', 'date', 'exam_id', 'offer_id')

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('exam_id', 'pet', 'vet', 'date', 'cost', 'heart_rate', 'respiration_rate', 'temperature', 'comments', 'diagnosis')

class ConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conditions
        fields = ('condition_id', 'name', 'keywords', 'description') 

class SymptomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptoms
        fields = ('symptom_id', 'name', 'description',
                'aggression',
                'alopecia',
                'back_sensitivity',
                'bad_breath',
                'bald_patches',
                'biting_skin',
                'black_stool',
                'bladder_infection',
                'bleeding',
                'bloating',
                'blood_in_mouth',
                'blood_in_urine',
                'bloody_stool',
                'blue_or_purple_tinge_to_tongue_or_gums',
                'breathing_problems',
                'brown_particles',
                'bumps_on_skin',
                'changes_in_eating_habits',
                'cloudy_pupils',
                'clumsiness',
                'coughing',
                'dehydration',
                'depression',
                'dialated_pupils',
                'diarrhea',
                'difficult_sitting',
                'difficulty_breathing',
                'difficulty_moving',
                'difficulty_urinating',
                'discharge',
                'discolored_skin',
                'discolored_teeth',
                'dizziness',
                'dry_skin',
                'dull_coat',
                'ear_inflammation',
                'ear_irritation',
                'excessive_bleeding',
                'excessive_bruising',
                'excessive_drinking',
                'excessive_drooling',
                'excessive_ear_wax',
                'excessive_panting',
                'excessive_scratching',
                'excessively_odorous_stool',
                'excessive_saliva',
                'eye_discharge',
                'eye_inflammation',
                'eye_irritation',
                'eye_redness',
                'facial_swelling',
                'fainting',
                'fever',
                'flea_dirt',
                'frequent_urination',
                'grouchiness',
                'hair_loss',
                'head_shaking',
                'hearing_loss',
                'heart_murmur',
                'impaired_vision',
                'incontenince',
                'increased_urination',
                'inflammation',
                'insomnia',
                'irritability',
                'itchy_eye',
                'kidney_infection',
                'kidney_stones',
                'lethargy',
                'licking_skin',
                'limping',
                'loose_teeth',
                'loss_of_appetite',
                'lumps_under_skin',
                'mucus_in_stool',
                'muscle_atrophy',
                'muscle_loss',
                'nasal_discharge',
                'nose_bleed',
                'nose_discharge',
                'odorous_discharge',
                'odorous_ear',
                'odorous_skin',
                'oozing_pus',
                'pacing',
                'pale_gums',
                'pale_tongue',
                'pawing_at_face',
                'pressing_head_against_wall',
                'raised_leg',
                'rapid_heartbeat',
                'rash',
                'receeding_gums',
                'red_gums',
                'restlessness',
                'scabs',
                'scaly_skin',
                'seizures',
                'sensitive_elbow',
                'sensitive_hip',
                'sensitive_to_cold_air',
                'sensitivity',
                'shaking',
                'skin_flakes',
                'skin_irritation',
                'skin_lesions',
                'skin_redness',
                'skin_yellowing',
                'sneezing',
                'snorting',
                'sores',
                'swelling',
                'swelling_in_abdomen',
                'swelling_in_elbow',
                'swelling_in_hip',
                'swollen_gums',
                'swollen_lymph_nodes',
                'teeth_loss',
                'thick_red_bump_in_corner_of_eye',
                'thickening_of_skin',
                'ticks_on_skin',
                'trembling_hind_legs',
                'unable_to_jump',
                'underdeveloped_growth',
                'unsual_sleeping_patterns',
                'visible_fleas',
                'vomiting',
                'weight_gain',
                'weight_loss',
                'wheezing',
                'whining',
                'white_foamy_vomit',
                'worm_in_stool')

