from csv import unregister_dialect
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.conf import settings

#This file defines the automated creation of Djangos mysql database. These classes are 
#automatically converted into mysql by Django. Each class loosely represents a table in the database,
#with variables as columns.






class Account(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    account_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zipcode = models.IntegerField()


class Pet_Owner(models.Model):
    user_id = models.OneToOneField(Account,
            on_delete = models.CASCADE,
            primary_key=True)
    address = models.CharField(max_length = 100)

#DEPRECIATED

#class Dog(models.Model):
#    breed = models.CharField(max_length = 100)
#
#class Cat(models.Model):
#    breed = models.CharField(max_length = 100)
#    declawed = models.BooleanField()
#
#    class Meta:
#        unique_together = (('breed',
#        'declawed'))
#
#


class Veterinarian(models.Model):
    vet_id = models.OneToOneField(Account, 
                on_delete = models.CASCADE,
                primary_key = True)
    name = models.CharField(max_length = 100)





class Conditions(models.Model):
    condition_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    keywords = models.CharField(max_length = 100)
    description = models.CharField(max_length = 5000)

class Pets(models.Model):
    pet_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)
    dob = models.CharField(max_length = 100)
    reproductive_status = models.BooleanField()
    had_kids = models.BooleanField()
    weight = models.IntegerField()
    height = models.IntegerField()
    age = models.IntegerField()
    conditions = models.ManyToManyField(Conditions)
    owner = models.ForeignKey(Pet_Owner, on_delete = models.CASCADE)
    type = [('Cat','Cat'),('Dog','Dog'),]



class Exam(models.Model):
    exam_id = models.AutoField(primary_key = True)
    pet = models.ForeignKey(Pets,default=1,
                                on_delete = models.CASCADE)
    vet = models.ForeignKey(Veterinarian,
                                on_delete = models.CASCADE)
    date = models.DateTimeField()
    cost = models.IntegerField()
    heart_rate = models.IntegerField()
    respiration_rate = models.IntegerField()
    temperature = models.IntegerField()
    comments = models.CharField(max_length = 5000)
    diagnosis = models.CharField(max_length = 5000)

class Symptoms(models.Model):
    symptom_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)

    aggression = models.BooleanField(default = False)
    alopecia = models.BooleanField(default = False)
    back_sensitivity = models.BooleanField(default = False)
    bad_breath = models.BooleanField(default = False)
    bald_patches = models.BooleanField(default = False)
    biting_skin = models.BooleanField(default = False)
    black_stool = models.BooleanField(default = False)
    bladder_infection = models.BooleanField(default = False)
    bleeding = models.BooleanField(default = False)
    bloating = models.BooleanField(default = False)
    blood_in_mouth = models.BooleanField(default = False)
    blood_in_urine = models.BooleanField(default = False)
    bloody_stool = models.BooleanField(default = False)
    blue_or_purple_tinge_to_tongue_or_gums = models.BooleanField(default = False)
    breathing_problems = models.BooleanField(default = False)
    brown_particles = models.BooleanField(default = False)
    bumps_on_skin = models.BooleanField(default = False)
    changes_in_eating_habits = models.BooleanField(default = False)
    cloudy_pupils = models.BooleanField(default = False)
    clumsiness = models.BooleanField(default = False)
    coughing = models.BooleanField(default = False)
    dehydration = models.BooleanField(default = False)
    depression = models.BooleanField(default = False)
    dialated_pupils = models.BooleanField(default = False)
    diarrhea = models.BooleanField(default = False)
    difficult_sitting = models.BooleanField(default = False)
    difficulty_breathing = models.BooleanField(default = False)
    difficulty_moving = models.BooleanField(default = False)
    difficulty_urinating = models.BooleanField(default = False)
    discharge = models.BooleanField(default = False)
    discolored_skin = models.BooleanField(default = False)
    discolored_teeth = models.BooleanField(default = False)
    dizziness = models.BooleanField(default = False)
    dry_skin = models.BooleanField(default = False)
    dull_coat = models.BooleanField(default = False)
    ear_inflammation = models.BooleanField(default = False)
    ear_irritation = models.BooleanField(default = False)
    excessive_bleeding = models.BooleanField(default = False)
    excessive_bruising = models.BooleanField(default = False)
    excessive_drinking = models.BooleanField(default = False)
    excessive_drooling = models.BooleanField(default = False)
    excessive_ear_wax = models.BooleanField(default = False)
    excessive_panting = models.BooleanField(default = False)
    excessive_scratching = models.BooleanField(default = False)
    excessively_odorous_stool = models.BooleanField(default = False)
    excessive_saliva = models.BooleanField(default = False)
    eye_discharge = models.BooleanField(default = False)
    eye_inflammation = models.BooleanField(default = False)
    eye_irritation = models.BooleanField(default = False)
    eye_redness = models.BooleanField(default = False)
    facial_swelling = models.BooleanField(default = False)
    fainting = models.BooleanField(default = False)
    fever = models.BooleanField(default = False)
    flea_dirt = models.BooleanField(default = False)
    frequent_urination = models.BooleanField(default = False)
    grouchiness = models.BooleanField(default = False)
    hair_loss = models.BooleanField(default = False)
    head_shaking = models.BooleanField(default = False)
    hearing_loss = models.BooleanField(default = False)
    heart_murmur = models.BooleanField(default = False)
    impaired_vision = models.BooleanField(default = False)
    incontenince = models.BooleanField(default = False)
    increased_urination = models.BooleanField(default = False)
    inflammation = models.BooleanField(default = False)
    insomnia = models.BooleanField(default = False)
    irritability = models.BooleanField(default = False)
    itchy_eye = models.BooleanField(default = False)
    kidney_infection = models.BooleanField(default = False)
    kidney_stones = models.BooleanField(default = False)
    lethargy = models.BooleanField(default = False)
    licking_skin = models.BooleanField(default = False)
    limping = models.BooleanField(default = False)
    loose_teeth = models.BooleanField(default = False)
    loss_of_appetite = models.BooleanField(default = False)
    lumps_under_skin = models.BooleanField(default = False)
    mucus_in_stool = models.BooleanField(default = False)
    muscle_atrophy = models.BooleanField(default = False)
    muscle_loss = models.BooleanField(default = False)
    nasal_discharge = models.BooleanField(default = False)
    nose_bleed = models.BooleanField(default = False)
    nose_discharge = models.BooleanField(default = False)
    odorous_discharge = models.BooleanField(default = False)
    odorous_ear = models.BooleanField(default = False)
    odorous_skin = models.BooleanField(default = False)
    oozing_pus = models.BooleanField(default = False)
    pacing = models.BooleanField(default = False)
    pale_gums = models.BooleanField(default = False)
    pale_tongue = models.BooleanField(default = False)
    pawing_at_face = models.BooleanField(default = False)
    pressing_head_against_wall = models.BooleanField(default = False)
    raised_leg = models.BooleanField(default = False)
    rapid_heartbeat = models.BooleanField(default = False)
    rash = models.BooleanField(default = False)
    receeding_gums = models.BooleanField(default = False)
    red_gums = models.BooleanField(default = False)
    restlessness = models.BooleanField(default = False)
    scabs = models.BooleanField(default = False)
    scaly_skin = models.BooleanField(default = False)
    seizures = models.BooleanField(default = False)
    sensitive_elbow = models.BooleanField(default = False)
    sensitive_hip = models.BooleanField(default = False)
    sensitive_to_cold_air = models.BooleanField(default = False)
    sensitivity = models.BooleanField(default = False)
    shaking = models.BooleanField(default = False)
    skin_flakes = models.BooleanField(default = False)
    skin_irritation = models.BooleanField(default = False)
    skin_lesions = models.BooleanField(default = False)
    skin_redness = models.BooleanField(default = False)
    skin_yellowing = models.BooleanField(default = False)
    sneezing = models.BooleanField(default = False)
    snorting = models.BooleanField(default = False)
    sores = models.BooleanField(default = False)
    swelling = models.BooleanField(default = False)
    swelling_in_abdomen = models.BooleanField(default = False)
    swelling_in_elbow = models.BooleanField(default = False)
    swelling_in_hip = models.BooleanField(default = False)
    swollen_gums = models.BooleanField(default = False)
    swollen_lymph_nodes = models.BooleanField(default = False)
    teeth_loss = models.BooleanField(default = False)
    thick_red_bump_in_corner_of_eye = models.BooleanField(default = False)
    thickening_of_skin = models.BooleanField(default = False)
    ticks_on_skin = models.BooleanField(default = False)
    trembling_hind_legs = models.BooleanField(default = False)
    unable_to_jump = models.BooleanField(default = False)
    underdeveloped_growth = models.BooleanField(default = False)
    unsual_sleeping_patterns = models.BooleanField(default = False)
    visible_fleas = models.BooleanField(default = False)
    vomiting = models.BooleanField(default = False)
    weight_gain = models.BooleanField(default = False)
    weight_loss = models.BooleanField(default = False)
    wheezing = models.BooleanField(default = False)
    whining = models.BooleanField(default = False)
    white_foamy_vomit = models.BooleanField(default = False)
    worm_in_stool = models.BooleanField(default = False)

    description = models.CharField(max_length = 5000)
    

class Appointment_Offer(models.Model):
    offer_id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(Pet_Owner, 
                                on_delete = models.CASCADE)
    pet_id = models.CharField(max_length = 100)
    date = models.DateTimeField()
    symptoms_id = models.OneToOneField(Symptoms,
                                        on_delete = models.CASCADE)

    activeRequest = models.BooleanField(default = True)


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Pet_Owner,
                                on_delete = models.CASCADE)
    pet_id = models.CharField(max_length = 100)
    vet_id = models.ForeignKey(Veterinarian,
                                on_delete = models.CASCADE)
    location = models.CharField(max_length = 100)
    date = models.DateTimeField()
    exam_id = models.OneToOneField(Exam, 
                                    on_delete = models.CASCADE)
    offer_id = models.OneToOneField(Appointment_Offer,
                                    on_delete = models.CASCADE)