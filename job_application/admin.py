from django.contrib import admin
from .models import Form


class FormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date', 'occupation')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('date', 'occupation')
    ordering = ('first_name',)
    readonly_fields = ('date',)

# Register your models here.
admin.site.register(Form, FormAdmin)
