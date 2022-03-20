
#admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'nickname')
    list_display_links = ['username', 'nickname']
    search_fields = ['username', 'nickname']
    fieldsets = (
        ('ID & PW', {'fields': ('username', 'password')}),
        ('Info', {'fields': ('nickname', 'date_joined')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'nickname', 'password1', 'password2')}
         ),
    )


admin.site.register(User, UserAdmin)

