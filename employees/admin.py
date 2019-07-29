from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _

from employees.models import Employee, Barber
from employees.forms import BarberAdminForm


@admin.register(Employee)
class EmployeeAdmin(BaseUserAdmin):
    list_display = (
        '__str__',
        'username',
        'type',
        'email',
        'last_login',
        'is_active',
    )
    list_display_links = ('__str__', 'username',)
    list_filter = ('type', 'last_login',)
    search_fields = ('first_name', 'last_name', 'username', 'email',)
    ordering = ('first_name', 'last_name',)

    def get_fieldsets(self, request, obj=None):
        title = _('Employee info')
        exists = any([v for v in self.fieldsets if v[0] == title])
        if not exists:
            emp_fieldsets = ((title, {'fields': ('type', 'photo',)}),)
            self.fieldsets = self.fieldsets[:1] + emp_fieldsets + self.fieldsets[1:]
        return super().get_fieldsets(request, obj)


@admin.register(Barber)
class BarberAdmin(BaseUserAdmin):
    list_display = (
        '__str__',
        'username',
        'type',
        'email',
        'last_login',
        'is_active',
    )
    list_display_links = ('__str__', 'username',)
    list_filter = ('type', 'last_login',)
    search_fields = ('first_name', 'last_name', 'username', 'email',)
    ordering = ('first_name', 'last_name',)
    form = BarberAdminForm
    fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'photo', 'commission')}),
        (_('Permissions'), {
            'fields': ('is_active',),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            user_fields = ('username', 'password1', 'password2')
        else:
            user_fields = ('username', 'password')
        self.fieldsets[0][1]['fields'] = user_fields
        return super().get_fieldsets(request, obj)
