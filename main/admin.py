from django.contrib import admin

from .models import *


class Document_admin(admin.ModelAdmin):
    list_display = ('name', 'date', 'organization', 'invoice', 'article', 'analytics', 'amount', 'time_create', 'time_update', )
    exclude = ('author', 'is_published', )

class Organization_admin(admin.ModelAdmin):
    list_display = ('name', 'description')


class Invoice_admin(admin.ModelAdmin):
    list_display = ('name', 'description')


class Article_admin(admin.ModelAdmin):
    list_display = ('name', 'description')


class Analytics_admin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Document, Document_admin)
admin.site.register(Organization, Organization_admin)
admin.site.register(Invoice, Invoice_admin)
admin.site.register(Article, Article_admin)
admin.site.register(Analytics, Analytics_admin)
