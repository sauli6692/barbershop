from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


class BarbershopOffering(models.Model):
    name = models.CharField(_('Name'), max_length=150)
    description = models.CharField(_('Description'), max_length=255)
    price = models.DecimalField(_('Price'), max_digits=5, decimal_places=2)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name} - {self.price}'



class Service(BarbershopOffering):
    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')


class BarberService(models.Model):
    barber = models.ForeignKey(
        'employees.Barber',
        verbose_name=_('Barber'),
        on_delete=models.CASCADE,
        related_name='services_performed',
    )
    service = models.ForeignKey(
        Service,
        verbose_name=_('Service'),
        on_delete=models.CASCADE,
        related_name='barber_service',
    )
    price = models.DecimalField(_('Price'), max_digits=6, decimal_places=2)
    discount_percentage = models.IntegerField(
        _('Discount Percentage'),
        default=0,
    )
    performed = models.DateTimeField(
        _('Performed date'),
        auto_now_add=True,
    )

    @property
    def discount(self):
        return self.price * self.discount_percentage / 100

    @property
    def total(self):
        return self.price - self.discount


class Product(BarbershopOffering):
    quantity = models.IntegerField(_('Quantity'))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Invoice(models.Model):
    employee = models.ForeignKey(
        'employees.Employee',
        verbose_name=_('Employee'),
        on_delete=models.CASCADE
    )
    issued = models.DateTimeField(_('Issued date'), auto_now_add=True)


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        verbose_name=_('Invoice'),
        on_delete=models.CASCADE,
        related_name='details',
    )
    product = models.ForeignKey(
        Product,
        verbose_name=_('Product'),
        on_delete=models.CASCADE,
        related_name='invoices_details',
    )
    unit_price = models.DecimalField(
        _('Unit Price'),
        max_digits=6,
        decimal_places=2,
    )
    quantity = models.IntegerField(
        _('Quantity'),
        default=1,
    )
    discount_percentage = models.IntegerField(
        _('Discount Percentage'),
        default=0,
    )

    @property
    def sub_total(self):
        if not hasattr(self, '_sub_total'):
            self._sub_total = self.unit_price * self.quantity

        return self._sub_total

    @property
    def discount(self):
        return self.sub_total * self.discount_percentage / 100

    @property
    def total(self):
        return self.sub_total - self.discount
