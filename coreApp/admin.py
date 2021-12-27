from django.contrib import admin
from .models import *

class BaseModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    empty_value_display = '-'
    date_hierarchy = 'created_at'

