from django.contrib.auth.forms import UserCreationForm, UsernameField

from employees.models import Barber


class BarberAdminForm(UserCreationForm):
    class Meta:
        model = Barber
        fields = '__all__'
        field_classes = {'username': UsernameField}
