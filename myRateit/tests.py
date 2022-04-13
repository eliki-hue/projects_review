from django.test import TestCase

# from myGallery.models import Image
from myRateit.models import Profile, Project
# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        self.new_profile =Profile('','','','','')

    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)
        

    def test_updating(self):
        self.new_profile.update_profile('test_profile','test_profile2')
        self.assertFalse(Profile.objects.filter(name='test_profile2').exists())

    def test_delete_profile(self):       
        self.new_profile.delete_profile('test_profile')           
        self.assertFalse(Profile.objects.filter(name='test_profile').exists())




class ProjectTestClass(TestCase):
    def setUp(self):
        self.post=Project(title='Project1')
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Project))
