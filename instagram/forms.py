from django import forms
from .models import Profile, Image


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'profile_pic']


class UploadUserImages(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes', 'dislikes', 'comments', 'posted_on', 'profile']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['dislikes', 'posted_on', 'profile', 'image_name', 'image', 'image_caption']
