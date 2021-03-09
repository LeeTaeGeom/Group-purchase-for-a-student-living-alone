from django.contrib import admin

# Register your models here.
from django.contrib import admin
from funding.models import Funding

class FundingAdmin(admin.ModelAdmin):
    list_display='__all__'

admin.site.register(Funding, FundingAdmin)
