from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


admin.site.register(Contact, ContactAdmin)
