from django.contrib import admin
<<<<<<< HEAD
from authentication.models import RegistrationCode
from datetime import datetime

# Register your models here.

def delete_past_due_codes(modeladmin, request, queryset):
    queryset.filter(expiry_date__lt=datetime.today()).delete()
delete_past_due_codes.short_description = "Delete all codes that are past due."

class RegistrationCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'expiry_date', 'used_by',]
    ordering = ['-expiry_date']
    actions = [delete_past_due_codes]

admin.site.register(RegistrationCode, RegistrationCodeAdmin)
=======

# Register your models here.
>>>>>>> 35d2739b1827ff3da2a5b12e6021f53fb0de5e43
