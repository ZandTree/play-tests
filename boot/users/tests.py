from django.test import TestCase

from users.models import User


class BasicUser(TestCase):
    def setUp(self) -> None:
        self.user = User()
        self.user.username = 'Mio'
        self.user.email = 'mio@mail.com'
        self.user.save()

    def test_fields(self):
        """ check methods to set boelean attrs to True"""
        user_record = User.objects.get(pk=self.user.id)

        self.assertEqual(user_record, self.user)
        self.assertEqual(user_record.banned, False)
        self.assertEqual(user_record.blackListEmail, False)

        user_record.set_banned()
        user_record.put_to_black_mail_list()

        self.assertEqual(user_record.banned, True)
        self.assertEqual(user_record.blackListEmail, True)
