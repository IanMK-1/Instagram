from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    profile_pic = CloudinaryField('image', null=True)
    bio = models.TextField()
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.bio
