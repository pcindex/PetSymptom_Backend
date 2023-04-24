from django.test import TestCase

from api.models import *

#These classes test the creation, retrieval, and model key connections of User, Account, PetOwner, Pet, and Condition
#
#

#Account Creation Test

class AccountCreationTest(TestCase):
    def testcreation(self):
        self.TestUser = User.objects.create(username = 'TestCase',password = 'password')
        self.TestUser.save()
        self.Acc = Account.objects.create(
           account_id = 1,
            phone_number = '5151234567',
            email = 'testemail@gmail.com',
            city = 'Ames',
            state = 'Iowa',
            zipcode = '50014',
            user = self.TestUser
        )
        self.Acc.save()
        self.cond = condition = Conditions.objects.create(
            name = 'testname',
            keywords = 'test',
            description = 'test'
        )
        self.cond.save()

        account = Account.objects.get(email = "testemail@gmail.com")
        self.assertEqual(account.account_id, 1)
        self.assertEqual(account.user.username, 'TestCase')
        

#Account Information Population Tests
class AccountPopulationTest(TestCase):
    def testcreation(self):
        TestUser = User.objects.create(username = 'TestCase',password = 'password')
        Account.objects.create(
            account_id = 1,
            phone_number = '5151234567',
            email = 'testemail@gmail.com',
            city = 'Ames',
            state = 'Iowa',
            zipcode = '50014',
            user = TestUser
        )

        Owner = Pet_Owner.objects.create(
            user_id = Account.objects.get(email = 'testemail@gmail.com'),
            address = 'Ames ave'
        )
        conditionset = Conditions.objects.create(
            name = 'Cutitis',
            keywords = 'Cute, Love',
            description = 'Way too cute!'
        )
        Pet = Pets.objects.create(
            name = "Testy",
            dob = '5/30/2000',
            reproductive_status = False ,
            had_kids = True,
            weight = 20,
            height = 10,
            age = 4,
            owner = Pet_Owner.objects.get(user_id = Account.objects.get(email = 'testemail@gmail.com'))

        )
        Pet.conditions.set(Conditions.objects.filter(name = 'Cutitis'))


        account = Account.objects.get(email = 'testemail@gmail.com')
        Pet_Own = Pet_Owner.objects.get(user_id = account.account_id)
        PetName = Pets.objects.get(owner = Pet_Own).name
        PetCondition = Pets.objects.get(owner = Pet_Own).conditions.first().name

        self.assertEqual(PetCondition,'Cutitis')
        self.assertEqual(PetName, 'Testy')


        

