from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Register your models here.

# Define an inline admin descriptor for UserProfile model
# Allows edits to the model on the same page as a parent model
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name = "User Profile"

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UserProfileInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)