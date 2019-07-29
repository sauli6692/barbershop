from django.utils.translation import ugettext_lazy as _


USER_TYPE_STAFF = 'STAFF'
USER_TYPE_ADMIN = 'ADMIN'
USER_TYPE_BARBER = 'BARBER'
USER_TYPE_CHOICES = (
    (USER_TYPE_STAFF, _('Dev')),
    (USER_TYPE_ADMIN, _('Admin')),
    (USER_TYPE_BARBER, _('Barber')),
)