from django.contrib import admin
from django.contrib.auth.models import Group
from .forms import GroupAdminForm
from .models import Casting
from accounts.models import Profile


admin.site.unregister(Group)


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    filter_horizontal = ['permissions']


admin.site.register(Group, GroupAdmin)
admin.site.register(Casting)
admin.site.register(Profile)
