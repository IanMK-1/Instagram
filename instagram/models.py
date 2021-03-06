from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    profile_pic = CloudinaryField('image', null=True)
    bio = models.TextField(blank=True)
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.bio

    def save_user_profile(self):
        self.save()

    def delete_user_profile(self):
        self.delete()

    @classmethod
    def update_profile_bio(cls, id, bio):
        cls.objects.filter(id=id).update(bio=bio)
        updated_profile_bio = cls.objects.get(id=id)
        return updated_profile_bio

    @classmethod
    def update_profile_pic(cls, id, profile_pic):
        cls.objects.filter(id=id).update(profile_pic=profile_pic)
        updated_profile_pic = cls.objects.get(id=id)
        return updated_profile_pic


class Image(models.Model):
    image = CloudinaryField('image', null=True)
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=50)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    comments = models.CharField(max_length=500, null=True, blank=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls, id, caption):
        cls.objects.filter(id=id).update(image_caption=caption)
        updated_caption = cls.objects.get(id=id)
        return updated_caption
