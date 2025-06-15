from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('user_type', 'profile_picture', 'address_line1', 'city', 'state', 'pincode')
        }),
    )
    list_display = ['username', 'email', 'user_type', 'first_name', 'last_name']
    list_filter = ['user_type']

admin.site.register(CustomUser, CustomUserAdmin)