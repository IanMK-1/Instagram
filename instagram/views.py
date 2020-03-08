from django.shortcuts import render
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@login_required(login_url='/accounts/login/')
def timeline(request):
    return render(request, 'timeline.html')


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    try:
        if current_user.is_authenticated:
            user_profile = Profile.objects.get(id=current_user.id)
            profile_images = Image.objects.filter(profile__id=current_user.id).all()
            all_following = user_profile.user.all()
            users = User.objects.all()
            number = 0
            for user in users:
                for specific_user_profile in user.profile_set.all():
                    for following_user in specific_user_profile.user.all():
                        if following_user.id == current_user.id:
                            number += 1
                        else:
                            number = 0

    except ObjectDoesNotExist:
        profile_images = None
        user_profile = None

    return render(request, 'profile.html',
                  {"user_profile": user_profile, "profile_images": profile_images, "current_user": current_user,
                   "all_following": all_following, "number": number})


def edit_profile(request):
    return render(request, 'edit_profile.html')
