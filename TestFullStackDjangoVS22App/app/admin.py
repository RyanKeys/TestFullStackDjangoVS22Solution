from django.contrib import admin
from .models import Client, Company, Job

class CompanyInline(admin.TabularInline):
    model = Company

class JobInline(admin.TabularInline):
    model = Job

class ClientInline(admin.TabularInline):
    model = Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', "email")
    inlines = [
    ]

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "primary_contact")
    inlines = [
    ]

class JobAdmin(admin.ModelAdmin):
    inlines = [
        CompanyInline
    ]
    
admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Client, ClientAdmin)
