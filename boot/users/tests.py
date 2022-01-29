from django.test import TestCase

from users.models import User

"""
username = models.CharField(_("Username"), unique=True, max_length=120)
    email = models.EmailField(_("Email"), unique=True)
    banned = models.BooleanField(default=False)
    blackListEmail = models.BooleanField(default=False)


"""


class BasicUser(TestCase):
    def test_fields(self):
        """ check whether user obj has 2 required fields"""
        obj = User()
        obj.username = 'Mio'
        obj.email ='mio@mail.com'
        obj.save()

        obj_record = User.objects.get(pk=1)
        self.assertEqual(obj_record,obj)
