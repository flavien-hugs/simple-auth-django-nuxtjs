# user.admin.py

from django.contrib import admin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    model = get_user_model()
    list_per_page = 10
    date_hierarchy = 'date_joined'
    list_display = [
        'phone',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_superuser',
        "date_joined",
    ]
    search_fields = ('phone',)
    readonly_fields = ['phone']
    list_display_links = ('phone',)
