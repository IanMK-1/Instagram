from django.contrib import admin
from .models import Image, Profile


class ProfileAdmin(admin.ModelAdmin):
    filter_horizontal = ('user',)


# Register your models here.
admin.site.register(Image)
admin.site.register(Profile, ProfileAdmin)
