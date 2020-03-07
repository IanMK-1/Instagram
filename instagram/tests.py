from django.test import TestCase
from .models import Image, Profile
from django.contrib.auth.models import User


# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self) -> None:
        # creating a new user and saving it
        self.new_user = User(password='weareone', username='ian', first_name='ian', last_name='mark',
                             email='imk@gmail.com')
        self.new_user.save()

        # creating a new profile and saving it
        self.new_profile = Profile(profile_pic='imk.jpg', bio='hello')
        self.new_profile.save()

        # creating a new image and saving it
        self.new_image = Image(image='color.jpg', image_name='colors', image_caption='beautiful colors', likes=1,
                               dislikes=0, comments='i like it', profile=self.new_profile)
        self.new_image.save()

    def tearDown(self) -> None:
        Image.objects.all().delete()
        User.objects.all().delete()
        Profile.objects.all().delete()

