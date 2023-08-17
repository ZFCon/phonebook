from django.contrib import admin
from book.models import PhoneNumber, Contact


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass