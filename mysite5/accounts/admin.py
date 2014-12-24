from django.contrib import admin
#from accounts.models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

#class ProfileInline(admin.StackedInline):
#    model = UserProfile

#class CustomUserAdmin(UserAdmin):
#    inlines = (ProfileInline,)

#admin.site.unregister(User)
#admin.site.register(User, CustomUserAdmin)
