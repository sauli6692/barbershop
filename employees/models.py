from os.path import splitext

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from sorl.thumbnail import ImageField

from employees.choices import (
    USER_TYPE_CHOICES,
    USER_TYPE_STAFF,
    USER_TYPE_ADMIN,
    USER_TYPE_BARBER,
)


def upload_to_profile(instance, filename):
    filename_base, filename_ext = splitext(filename)
    return f'employees/profile/{instance.username}{filename_ext.lower()}'

def upload_to_contract(instance, filename):
    filename_base, filename_ext = splitext(filename)
    return f'employees/contract/{instance.username}{filename_ext.lower()}'


class Employee(AbstractUser):
    type = models.CharField(
        _('User type'),
        max_length=6,
        choices=USER_TYPE_CHOICES,
        default=USER_TYPE_BARBER
    )
    photo = ImageField(
        _('Profile picture'),
        blank=True,
        upload_to=upload_to_profile
    )

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def save(self, *args, **kwargs):
        self.is_superuser == self.type == USER_TYPE_ADMIN
        self.is_staff = self.type == USER_TYPE_STAFF
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Barber(Employee):
    commission = models.IntegerField(
        _('Commission percentage'),
        default=35
    )
    contract_picture = ImageField(
        _('Contract picture'),
        blank=True,
        upload_to=upload_to_contract
    )

    class Meta:
        verbose_name = _('Barber')
        verbose_name_plural = _('Barbers')

    @property
    def commission_percentage(self):
        return self.commission / 100
