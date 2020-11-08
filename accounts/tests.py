from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()
# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
       user_a = User(username='abhinav', email='abhinavshashank008@gmail.com')
       user_a.is_staff = True
       user_a.is_superuser = True
       user_a.set_password('password')
       user_a.save()
       print(user_a.id)
    
    def test_user_count(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count,1)
        print(user_count)
        self.assertNotEqual(user_count,0)