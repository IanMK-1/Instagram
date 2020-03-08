from django.shortcuts import render
from .models import Image, Profile
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login/')
def timeline(request):
    return render(request, 'timeline.html')


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if current_user.is_authenticated:
        user_profile = Profile.objects.filter(id=current_user.id)
        profile_images = Image.objects.filter(profile__id=current_user.id)

    return render(request, 'profile.html',
                  {"user_profile": user_profile, "profile_images": profile_images, "current_user": current_user})


def edit_profile(request):
    return render(request, 'edit_profile.html')
