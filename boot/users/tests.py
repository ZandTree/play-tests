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
        print(self.user.username)
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
