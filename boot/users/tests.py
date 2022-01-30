from django.test import TestCase
from faker import Faker
from django.contrib.auth import get_user_model

User = get_user_model()


class BasicUser(TestCase):
    def setUp(self) -> None:
        self.faker = Faker()
        self.user = User.objects.create_user(
            username=self.faker.name().split(' ')[0],
            email=self.faker.email()
        )

        self.user.save()

    def tearDown(self) -> None:
        self.user.delete()

    def test_fields(self):
        """ check methods to set boolean attrs to True"""
        user_record = User.objects.get(pk=self.user.id)

        self.assertEqual(user_record, self.user)
        self.assertEqual(user_record.banned, False)
        self.assertEqual(user_record.blackListEmail, False)

        user_record.set_banned()
        user_record.put_to_black_mail_list()

        self.assertEqual(user_record.banned, True)
        self.assertEqual(user_record.blackListEmail, True)

        """
        self.faker.profile()
        print(self.faker.profile().get('job'))
        {'job': 'Animal technologist', 
        'company': 'Harvey-Hernandez', 
        'ssn': '556-31-4707', 
        'residence': '50400 Martinez Corners\nLake Susan, IA 91325', 
        'current_location': (Decimal('-59.034308'), 
        Decimal('0.796582')), 'blood_group': 'AB+', 
        'website': ['http://www.richardson-lee.net/', 
        'http://www.villa-gardner.com/', 'https://www.thomas.com/', 
        'http://jones.com/'], 'username': 'lgray', 
        'name': 'Benjamin West', 'sex': 'M', 'address': '973 Moore Ways Apt.
        218\nLake Ian, OR 17229', 'mail': 'matthewweber@hotmail.com', 
        'birthdate': datetime.date(1936, 6, 7)}        
        """
