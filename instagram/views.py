from django.shortcuts import render, redirect
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import EditProfileForm, UploadUserImages


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
            profile_images = Image.objects.filter(profile=user_profile).all()
            image_count = profile_images.count()
            all_following = user_profile.user.all()
            following_count = all_following.count()
            users = User.objects.all()
            followers_count = 0
            for user in users:
                for specific_user_profile in user.profile_set.all():
                    for following_user in specific_user_profile.user.all():
                        if following_user.id == current_user.id:
                            followers_count += 1
                        else:
                            followers_count = 0

    except ObjectDoesNotExist:
        profile_images = None
        user_profile = None
        all_following = None
        followers_count = 0
        image_count = 0
        following_count = 0

    return render(request, 'profile.html',
                  {"user_profile": user_profile, "profile_images": profile_images, "current_user": current_user,
                   "all_following": all_following, "followers_count": followers_count, "image_count": image_count,
                   "following_count": following_count})


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        current_user = request.user
        if form.is_valid():
            bio = form.cleaned_data['bio']
            Profile.update_profile_bio(current_user.id, bio)
            return redirect('Profile')
    else:
        form = EditProfileForm()

    return render(request, 'edit_profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def upload_images(request):
    if request.method == 'POST':
        form = UploadUserImages(request.POST, request.FILES)
        current_user = request.user
        if form.is_valid():
            image = form.cleaned_data['image']
            image_name = form.cleaned_data['image_name']
            image_caption = form.cleaned_data['image_caption']
            user_profile = Profile.objects.get(id=current_user.id)
            user_images = Image(image=image, image_name=image_name, image_caption=image_caption, profile=user_profile)
            user_images.save()
    else:
        form = UploadUserImages()

    return render(request, 'upload_images.html', {"form": form})


def search_results(request):
    try:
        if 'search_user' in request.GET and request.GET["search_user"]:
            search_term = request.GET.get("search_user")
            searched_users = User.objects.filter(username__icontains=search_term)

    except ObjectDoesNotExist:
        searched_users = None

    return render(request, 'search_results.html', {"users": searched_users, "search_item": search_term})
