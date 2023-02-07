from django.contrib import admin
from .models import Bug

# Register your models here.
class BugAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_open', 'handle_by')
    search_fields = ('title', 'is_open', 'handle_by')

admin.site.register(Bug, BugAdmin)