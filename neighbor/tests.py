from django.test import TestCase
from .models import Hood, Profile
from django.contrib.auth.models import User

# Create your tests here.
class HoodTestCase(TestCase):

    def test_instance(self):
        """
        This will test whether the new hood created is an instance of the Hood class
        """
        self.assertTrue(isinstance(self.new_hood, Hood))

    def test_save_hood(self):
        """
        This will test whether the new hood is added to the db
        """
        self.new_hood()
        self.assertTrue(len(Hood.objects.all()) > 0)

class ProfileTestCase(TestCase):
    
    def setUp(self):
        """
        This will add a new profile before each test
        """
        self.new_user = User()
        self.new_user.save()

