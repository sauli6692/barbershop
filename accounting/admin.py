from django.contrib import admin

from accounting.models import (
    Service,
    BarberService,
    Product,
    Invoice,
    InvoiceDetail,
)


class BarbershopOfferingAdmin(admin.ModelAdmin):
    class Meta:
        abstract = True

    list_display = (
        'name',
        'description',
        'price',
    )
    list_display_links = ('name',)
    search_fields = ('name', 'description', 'price', )
    ordering = ('name', 'price',)


@admin.register(Service)
class ServiceAdmin(BarbershopOfferingAdmin):
    pass


@admin.register(Product)
class ProductAdmin(BarbershopOfferingAdmin):
    pass


@admin.register(BarberService)
class BarberServiceAdmin(admin.ModelAdmin):
    list_display = (
        'service',
        'barber',
        'price',
        'discount'
    )
    list_display_links = ('service',)
    search_fields = ('price',)
    filter_fields = ('service', 'barber', 'performed',)
    ordering = ('performed',)
    autocomplete_fields = ('barber', 'service',)


class InvoiceDetailInline(admin.TabularInline):
    model = InvoiceDetail
    extra = 0


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'issued',
        'employee',
    )
    list_display_links = ('issued',)
    search_fields = ('issued',)
    filter_fields = ('employee', 'issued',)
    ordering = ('issued',)
    autocomplete_fields = ('employee',)

    inlines = (InvoiceDetailInline,)