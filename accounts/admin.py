from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'date_joined', 'last_login', 'is_staff')
    search_fields = ('username',)
    readonly_fields = ('date_joined', 'last_login', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)