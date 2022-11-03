from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class Account(UserAdmin):
    readonly_fields=('id', 'date_joined', 'last_login')

admin.site.register(User , Account) 