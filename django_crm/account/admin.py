from django.contrib import admin

from account.models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('email', 'first_name', 'last_name')

