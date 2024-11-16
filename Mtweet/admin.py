from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Meep

# Unregister Groups and User models
admin.site.unregister(Group)
admin.site.unregister(User)

class ProfileInline(admin.StackedInline):
    model = Profile

# Extend UserAdmin to customize User model in the admin
class UserAdmin(admin.ModelAdmin):
    model = User
    # Display only the username field on the admin page
    fields = ["username"]
    inlines = [ProfileInline]

# Register the customized UserAdmin and Profile model
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)

admin.site.register(Meep)
