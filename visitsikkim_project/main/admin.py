from django.contrib import admin
from .models import Monastery

@admin.register(Monastery)
class MonasteryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "description")
