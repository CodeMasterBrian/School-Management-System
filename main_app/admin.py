from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import *
# Register your models here.


# modify admin panel
# admin.site.site_header = "OPTICODE ADMIN PANEL" 
# admin.site.site_title = "COLLEGE MANAGEMENT SYSTEM"




class UserModel(UserAdmin):
    ordering = ('email',)


admin.site.register(CustomUser, UserModel)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Session)
