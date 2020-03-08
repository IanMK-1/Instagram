from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('timeline/', views.timeline, name='Timeline'),
    path('profile/', views.profile, name='Profile'),
    path('edit_profile/', views.edit_profile, name="Editprofile"),
    path('upload_images/', views.upload_images, name="Uploadimages"),
]
