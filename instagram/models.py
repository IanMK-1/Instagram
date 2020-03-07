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

    def save_user_profile(self):
        self.save()

    def delete_user_profile(self):
        self.delete()


class Image(models.Model):
    image = CloudinaryField('image', null=True)
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    comments = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name
