import email
from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display=('id','name','email','is_mvp','hire_date')
    list_display_links=('id','name')
    search_fields=('name','email')
    list_per_page=10

admin.site.register(Realtor,RealtorAdmin)